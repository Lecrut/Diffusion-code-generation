class WeightManager:
    def __init__(self):
        self._measurements = {}

    def store_weight(self, key, value):
        self._measurements[key] = value

    def get_weight(self, key):
        return self._measurements[key]

    def update_weight(self, key, value):
        if key not in self._measurements:
            raise KeyError(f"Measurement with key {key} does not exist")
        self._measurements[key] = value

    def get_all_measurements(self):
        return self._measurements.copy()

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("user_001", 70.5)
    manager.store_weight("user_002", 82.3)
    manager.update_weight("user_001", 69.8)
    print(manager.get_weight("user_001"))
    print(manager.get_weight("user_002"))
    print(manager.get_all_measurements())