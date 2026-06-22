class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, date: str, weight: float):
        self._weights[date] = weight

    def retrieve(self, date: str) -> float:
        return self._weights.get(date, None)

    def update(self, date: str, weight: float):
        self._weights[date] = weight

    def get_all_weights(self) -> dict:
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store("2023-10-01", 70.5)
    manager.store("2023-10-02", 70.2)
    manager.update("2023-10-02", 70.4)

    print(manager.retrieve("2023-10-01"))
    print(manager.retrieve("2023-10-02"))
    print(manager.retrieve("2023-10-03"))

    print(manager.get_all_weights())