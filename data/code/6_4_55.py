class WeightPairStore:
    def __init__(self):
        self.store = {}

    def add_pair(self, key, weight1, weight2):
        if not isinstance(key, str) or not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise ValueError("Invalid input types")
        self.store[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.store:
            raise ValueError(f"Key '{key}' not found in store")
        weight1, weight2 = self.store[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    wps = WeightPairStore()
    wps.add_pair('pairA', 45.5, 30.2)
    wps.add_pair('pairB', 60.0, 75.0)
    print(wps.get_difference('pairA'))
    print(wps.get_difference('pairB'))