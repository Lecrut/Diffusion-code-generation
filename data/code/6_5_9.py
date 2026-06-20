class WeightManager:
    def __init__(self):
        self._weights = {}

    def add_pair(self, label, weight1, weight2):
        self._weights[label] = (weight1, weight2)

    def get_difference(self, label):
        if label not in self._weights:
            raise KeyError(f"No weight pair found for label: {label}")
        w1, w2 = self._weights[label]
        return w1 - w2

if __name__ == '__main__':
    manager = WeightManager()
    manager.add_pair("pair_a", 150, 120)
    manager.add_pair("pair_b", 85, 90)
    manager.add_pair("pair_c", 200, 185)
    diff_a = manager.get_difference("pair_a")
    diff_b = manager.get_difference("pair_b")
    diff_c = manager.get_difference("pair_c")
    print(diff_a)
    print(diff_b)
    print(diff_c)