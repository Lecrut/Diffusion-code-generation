class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, date, weight):
        self._weights[date] = weight

    def retrieve_weight(self, date):
        return self._weights.get(date)

    def update_weight(self, date, new_weight):
        if date in self._weights:
            self._weights[date] = new_weight
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 70.5)
    manager.store_weight("2023-10-02", 71.0)
    manager.update_weight("2023-10-01", 70.2)
    retrieved_weight = manager.retrieve_weight("2023-10-01")
    print(retrieved_weight)
    all_weights = manager.get_all_weights()
    print(all_weights["2023-10-02"])