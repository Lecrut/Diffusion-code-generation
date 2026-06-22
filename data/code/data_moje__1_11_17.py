class WeightManager:
    def __init__(self):
        self.weights = {}

    def store(self, key, weight):
        self.weights[key] = weight

    def retrieve(self, key):
        return self.weights.get(key)

    def update(self, key, weight):
        if key in self.weights:
            self.weights[key] = weight

    def get_all(self):
        return dict(self.weights)

    def remove(self, key):
        if key in self.weights:
            del self.weights[key]

    def has_key(self, key):
        return key in self.weights

if __name__ == '__main__':
    manager = WeightManager()
    manager.store("alice", 150.5)
    manager.store("bob", 180.0)
    print(manager.retrieve("alice"))
    manager.update("alice", 148.2)
    print(manager.retrieve("alice"))
    print(manager.has_key("bob"))
    manager.remove("bob")
    print(manager.has_key("bob"))
    print(manager.get_all())