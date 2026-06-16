class CompoundManager:
    def __init__(self):
        self.weights = {}
    def add_compound(self, name, weight):
        self.weights[name] = weight
    def calculate_equivalent_weights(self, target_weight):
        total_equivalent_weight = 0
        for name, weight in self.weights.items():
            if weight != 0:
                ratio = weight / target_weight
                equivalent_weight = weight * ratio
                total_equivalent_weight += equivalent_weight
        return total_equivalent_weight
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("H2O", 18.015)
    manager.add_compound("NaCl", 58.44)
    manager.add_compound("C", 12.011)
    target = 100.0
    result = manager.calculate_equivalent_weights(target)
    print(f"Target weight: {target}")
    print(f"Total equivalent weight: {result}")