class WeightManager:

    def __init__(self):
        self.weights = {}

    def add_weight(self, key, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError('Weight must be a number')
        self.weights[key] = weight

    def get_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f'No weight found for key: {key}')
        if not isinstance(new_weight, (int, float)):
            raise ValueError('New weight must be a number')
        self.weights[key] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight('Alice', 60.5)
    wm.add_weight('Bob', 75.3)
    print(wm.get_weight('Alice'))
    wm.update_weight('Alice', 62.0)
    print(wm.get_weight('Alice'))