class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, identifier, weight):
        self.weights[identifier] = weight

    def retrieve_weight(self, identifier):
        return self.weights.get(identifier, None)

    def update_weight(self, identifier, delta):
        if identifier in self.weights:
            self.weights[identifier] += delta
            return True
        return False

    def delete_weight(self, identifier):
        if identifier in self.weights:
            del self.weights[identifier]
            return True
        return False

    def get_all_weights(self):
        return dict(self.weights)

    def get_average_weight(self):
        if not self.weights:
            return None
        total = sum(self.weights.values())
        count = len(self.weights)
        return total / count

    def get_max_weight(self):
        if not self.weights:
            return None
        return max(self.weights.values())

    def get_min_weight(self):
        if not self.weights:
            return None
        return min(self.weights.values())

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight('user1', 70.5)
    manager.store_weight('user2', 65.2)
    manager.store_weight('user3', 80.0)
    manager.update_weight('user1', 1.5)
    print(manager.retrieve_weight('user1'))
    print(manager.get_average_weight())
    print(manager.get_max_weight())
    print(manager.get_min_weight())
    print(manager.get_all_weights())
    manager.delete_weight('user2')
    print(manager.get_all_weights())
    print(manager.retrieve_weight('user4'))