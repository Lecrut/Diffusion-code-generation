class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, key, weight):
        self._weights[key] = weight

    def retrieve_weight(self, key):
        return self._weights.get(key)

    def update_weight(self, key, new_weight):
        if key in self._weights:
            self._weights[key] = new_weight
            return True
        return False

    def remove_weight(self, key):
        if key in self._weights:
            del self._weights[key]
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("day1", 75.5)
    manager.store_weight("day2", 76.0)
    manager.update_weight("day1", 75.2)
    day1_weight = manager.retrieve_weight("day1")
    print(day1_weight)
    all_weights = manager.get_all_weights()
    print(all_weights)