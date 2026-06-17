import datetime
class WeightReading:
    def __init__(self, timestamp, weight, system):
        self.timestamp = timestamp
        self.weight = weight
        self.system = system
    def __repr__(self):
        return f"WeightReading(timestamp={self.timestamp}, weight={self.weight}, system='{self.system}')"
if __name__ == '__main__':
    historical_weights = []
    readings_data = [
        (datetime.datetime(2023, 1, 1, 10, 0), 75.5, 'kg'),
        (datetime.datetime(2023, 1, 2, 14, 30), 75.8, 'kg'),
        (datetime.datetime(2023, 1, 3, 9, 0), 76.1, 'kg'),
        (datetime.datetime(2023, 1, 4, 18, 0), 75.9, 'kg'),
        (datetime.datetime(2023, 1, 5, 11, 0), 76.5, 'kg'),
    ]
    for ts, weight, system in readings_data:
        reading = WeightReading(ts, weight, system)
        historical_weights.append(reading)
    print("--- Stored Historical Weights ---")
    for reading in historical_weights:
        print(reading)
    print("\n--- Retrieval Example (Finding the latest reading) ---")
    if historical_weights:
        latest_reading = max(historical_weights, key=lambda r: r.timestamp)
        print(f"Latest Reading: {latest_reading}")