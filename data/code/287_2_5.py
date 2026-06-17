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
    reading2 = WeightReading(datetime.datetime(2023, 1, 2, 11, 30), 75.8, 'kg')
    reading3 = WeightReading(datetime.datetime(2023, 1, 3, 9, 0), 160.0, 'lbs')
    reading4 = WeightReading(datetime.datetime(2023, 1, 4, 14, 0), 75.6, 'kg')
    historical_weights.append(reading1)
    historical_weights.append(reading2)
    historical_weights.append(reading3)
    historical_weights.append(reading4)
    print("--- Stored Historical Weights ---")
    for reading in historical_weights:
        print(reading)
    print("\n--- Retrieving Specific Reading (Index 1) ---")
    if len(historical_weights) > 1:
        retrieved_reading = historical_weights[1]
        print(f"Timestamp: {retrieved_reading.timestamp}")
        print(f"Weight: {retrieved_reading.weight}")
        print(f"System: {retrieved_reading.system}")
    else:
        print("Not enough data to retrieve.")