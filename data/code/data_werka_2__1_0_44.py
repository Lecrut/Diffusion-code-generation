class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, key, weight):
        if not isinstance(key, str) or not isinstance(weight, (int, float)):
            raise ValueError('Invalid input types')
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f'Key {key} not found')
        if not isinstance(new_weight, (int, float)):
            raise ValueError('Invalid weight type')
        self.weights[key] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    print(wm.retrieve_weight('Alice'))
    wm.update_weight('Alice', 62.0)
    print(wm.retrieve_weight('Alice'))