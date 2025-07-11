from google.transit import gtfs_realtime_pb2
import csv

feed = gtfs_realtime_pb2.FeedMessage()
with open("VehiclePositions2.pb", "rb") as f:
    feed.ParseFromString(f.read())

with open("vehicle_positions.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Vehicle ID", "Trip ID", "Latitude", "Longitude", "Speed", "Timestamp"])
    
    for entity in feed.entity:
        if entity.HasField("vehicle"):
            v = entity.vehicle
            writer.writerow([
                v.vehicle.id,
                v.trip.trip_id,
                v.position.latitude,
                v.position.longitude,
                v.position.speed,
                v.timestamp
            ])

print("Saved as vehicle_positions.csv")
