class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_measurement(self, person_id, weight):
        self._weights[person_id] = weight

    def get_measurement(self, person_id):
        return self._weights.get(person_id)

    def update_measurement(self, person_id, weight):
        if person_id in self._weights:
            self._weights[person_id] = weight
            return True
        return False

    def get_all_measurements(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_measurement("user_001", 75.5)
    manager.store_measurement("user_002", 82.0)
    print(manager.get_measurement("user_001"))
    print(manager.update_measurement("user_001", 74.2))
    print(manager.get_measurement("user_001"))
    print(manager.get_all_measurements())