class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, key, weight):
        if not isinstance(key, str) or not isinstance(weight, (int, float)):
            raise ValueError('Invalid input types')
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f"Key '{key}' not found")
        if not isinstance(new_weight, (int, float)):
            raise ValueError('New weight must be a number')
        self.weights[key] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    wm.store_weight('Bob', 75.2)
    print(wm.retrieve_weight('Alice'))
    try:
        wm.update_weight('Charlie', 80.0)
    except KeyError as e:
        print(e)