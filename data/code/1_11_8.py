class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, person, weight):
        self.weights[person] = weight

    def retrieve_weight(self, person):
        return self.weights.get(person)

    def update_weight(self, person, weight):
        if person in self.weights:
            self.weights[person] = weight
            return True
        return False

    def get_all_weights(self):
        return dict(self.weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("Alice", 65.5)
    manager.store_weight("Bob", 78.2)
    print(manager.retrieve_weight("Alice"))
    print(manager.update_weight("Alice", 67.0))
    print(manager.retrieve_weight("Alice"))
    print(manager.get_all_weights())