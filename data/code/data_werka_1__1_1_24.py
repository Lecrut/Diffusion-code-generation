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
    wm = WeightManager()
    wm.add_weight('Alice', 60.5)
    wm.add_weight('Bob', 75.3)
    print(wm.get_weight('Alice'))
    updated = wm.update_weight('Bob', 78.2)
    print(updated)
    print(wm.get_weight('Bob'))