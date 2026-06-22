class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, label, value):
        self._weights[label] = value

    def get_weight(self, label):
        return self._weights.get(label, None)

    def update_weight(self, label, new_value):
        if label in self._weights:
            self._weights[label] = new_value
            return True
        return False

    def remove_weight(self, label):
        if label in self._weights:
            del self._weights[label]
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("week1", 150.5)
    manager.store_weight("week2", 149.0)
    manager.update_weight("week1", 150.0)
    current_weight = manager.get_weight("week1")
    all_weights = manager.get_all_weights()
    print(current_weight)
    print(all_weights)