class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, date, weight):
        self._weights[date] = weight

    def get(self, date):
        return self._weights[date]

    def update(self, date, weight):
        self._weights[date] = weight

    def get_all(self):
        return self._weights.copy()

if __name__ == '__main__':
    manager = WeightManager()
    manager.store('2023-01-01', 70.5)
    manager.store('2023-01-02', 70.2)
    manager.update('2023-01-01', 71.0)
    retrieved_weight = manager.get('2023-01-01')
    all_weights = manager.get_all()
    print(retrieved_weight)
    print(all_weights)