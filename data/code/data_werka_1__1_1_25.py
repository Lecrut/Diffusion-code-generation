class WeightManager:

    def __init__(self):
        self.weights = {}

    def add_weight(self, key, weight):
        self.weights[key] = weight

    def get_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key in self.weights:
            self.weights[key] = new_weight
            return True
        return False
if __name__ == '__main__':
    manager = WeightManager()
    manager.add_weight('Alice', 60)
    manager.add_weight('Bob', 75)
    print(manager.get_weight('Alice'))
    print(manager.update_weight('Alice', 62))
    print(manager.get_weight('Alice'))
    print(manager.get_weight('Charlie'))