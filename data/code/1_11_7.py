class WeightManager:
    def __init__(self):
        self._measurements = {}

    def _validate_weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a numeric value")
        if value < 0:
            raise ValueError("Weight cannot be negative")

    def store_measurement(self, timestamp, value):
        self._validate_weight(value)
        self._measurements[timestamp] = float(value)
        return True

    def fetch_measurement(self, timestamp):
        return self._measurements.get(timestamp)

    def modify_measurement(self, timestamp, new_value):
        self._validate_weight(new_value)
        if timestamp not in self._measurements:
            return False
        self._measurements[timestamp] = float(new_value)
        return True

    def list_all_measurements(self):
        return dict(self._measurements)

    def get_latest_record(self):
        if not self._measurements:
            return None
        sorted_timestamps = sorted(self._measurements.keys(), reverse=True)
        latest_key = sorted_timestamps[0]
        return (latest_key, self._measurements[latest_key])

if __name__ == '__main__':
    wm = WeightManager()
    wm.store_measurement("2023-10-01T08:00", 150.5)
    wm.store_measurement("2023-10-02T08:00", 149.2)
    wm.store_measurement("2023-10-03T08:00", 148.0)
    updated = wm.modify_measurement("2023-10-02T08:00", 149.5)
    print("Update success:", updated)
    print("Latest record:", wm.get_latest_record())
    print("All data:", wm.list_all_measurements())