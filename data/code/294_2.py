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
                equivalent_weight = weight * (target_weight / target_weight)                                                                                                                                    
                total_equivalent_weight += weight
        return total_equivalent_weight
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015)
    manager.add_compound("Methane", 16.043)
    manager.add_compound("Oxygen", 15.999)
    target = 50.0
    result = manager.calculate_equivalent_weights(target)
    print(f"Target Weight: {target}")
    print(f"Total Equivalent Weight Sum (based on individual weights): {result}")