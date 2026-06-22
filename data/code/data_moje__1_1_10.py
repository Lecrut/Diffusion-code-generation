class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, date, weight):
        self._weights[date] = weight

    def get_weight(self, date):
        return self._weights.get(date)

    def update_weight(self, date, weight):
        if date not in self._weights:
            return False
        self._weights[date] = weight
        return True

    def delete_weight(self, date):
        if date in self._weights:
            del self._weights[date]
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-01-01", 75.5)
    manager.store_weight("2023-01-02", 75.2)
    manager.store_weight("2023-01-03", 75.8)
    print(manager.get_weight("2023-01-02"))
    manager.update_weight("2023-01-02", 74.9)
    print(manager.get_weight("2023-01-02"))
    manager.delete_weight("2023-01-03")
    print(manager.get_weight("2023-01-03"))
    print(manager.get_all_weights())