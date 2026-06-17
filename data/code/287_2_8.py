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
    reading1 = WeightReading(datetime.datetime(2023, 1, 1, 10, 0), 75.5, 'kg')
    reading2 = WeightReading(datetime.datetime(2023, 1, 2, 14, 30), 75.8, 'kg')
    reading3 = WeightReading(datetime.datetime(2023, 1, 3, 9, 0), 160.0, 'lbs')
    reading4 = WeightReading(datetime.datetime(2023, 1, 4, 18, 0), 75.6, 'kg')
    historical_weights.append(reading1)
    historical_weights.append(reading2)
    historical_weights.append(reading3)
    historical_weights.append(reading4)
    print("--- Stored Historical Weights ---")
    for reading in historical_weights:
        print(reading)
    print("\n--- Retrieval Example (Finding all readings in kg) ---")
    kg_readings = [r for r in historical_weights if r.system == 'kg']
    for reading in kg_readings:
        print(reading)
    print("\n--- Retrieval Example (Finding a specific reading by timestamp) ---")
    target_time = datetime.datetime(2023, 1, 2, 14, 30)
    found_reading = None
    for reading in historical_weights:
        if reading.timestamp == target_time:
            found_reading = reading
            break
    if found_reading:
        print(f"Found reading at {target_time}: {found_reading}")
    else:
        print("Reading not found.")