class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, key, value):
        self.weights[key] = value

    def retrieve_weight(self, key):
        return self.weights.get(key)

    def update_weight(self, key, value):
        if key in self.weights:
            self.weights[key] = value
        else:
            raise KeyError(f"Key '{key}' not found")

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight('john', 75.5)
    manager.store_weight('jane', 62.3)
    print(manager.retrieve_weight('john'))
    manager.update_weight('john', 74.0)
    print(manager.retrieve_weight('john'))