class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, identifier, weight):
        self.weights[identifier] = weight

    def retrieve_weight(self, identifier):
        return self.weights.get(identifier)

    def update_weight(self, identifier, weight):
        if identifier in self.weights:
            self.weights[identifier] = weight
        else:
            self.weights[identifier] = weight

    def get_all_weights(self):
        return dict(self.weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("user1", 70.5)
    manager.store_weight("user2", 85.2)
    manager.update_weight("user1", 71.0)
    print(manager.retrieve_weight("user1"))
    print(manager.retrieve_weight("user2"))
    print(manager.get_all_weights())