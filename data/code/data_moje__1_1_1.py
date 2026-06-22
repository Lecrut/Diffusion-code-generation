class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, identifier, weight):
        self._weights[identifier] = weight

    def retrieve(self, identifier):
        return self._weights.get(identifier)

    def update(self, identifier, weight):
        if identifier not in self._weights:
            raise ValueError("Identifier not found")
        self._weights[identifier] = weight

    def get_all(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store("user1", 75.5)
    manager.store("user2", 80.0)
    print(manager.retrieve("user1"))
    manager.update("user1", 76.0)
    print(manager.retrieve("user1"))
    print(manager.get_all())