class MaterialCalculator:

    def __init__(self):
        self.densities = {'iron': 7.874, 'gold': 19.302, 'aluminum': 2.7, 'copper': 8.96}

    def calculate_weight(self, material, volume):
        density = self.densities.get(material.lower())
        if density is None:
            raise ValueError(f'Unknown material: {material}')
        return density * volume
if __name__ == '__main__':
    calculator = MaterialCalculator()
    print(calculator.calculate_weight('iron', 1))
    print(calculator.calculate_weight('gold', 0.5))
    print(calculator.calculate_weight('aluminum', 2))
    print(calculator.calculate_weight('copper', 3))