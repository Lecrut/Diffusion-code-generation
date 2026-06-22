class WeightManager:

    def __init__(self):
        self.weights = {}

    def add_weight(self, key, weight):
        if not isinstance(key, str) or not isinstance(weight, (int, float)):
            raise ValueError('Key must be a string and weight must be a number.')
        self.weights[key] = weight

    def get_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f"Weight with key '{key}' does not exist.")
        if not isinstance(new_weight, (int, float)):
            raise ValueError('New weight must be a number.')
        self.weights[key] = new_weight

    def remove_weight(self, key):
        if key not in self.weights:
            raise KeyError(f"Weight with key '{key}' does not exist.")
        del self.weights[key]
if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight('Alice', 60.5)
    wm.add_weight('Bob', 75.2)
    print(wm.get_weight('Alice'))
    wm.update_weight('Alice', 61.0)
    print(wm.get_weight('Alice'))
    wm.remove_weight('Bob')
    print(wm.get_weight('Bob'))