class MaterialCalculator:

    def __init__(self):
        self.densities = {'iron': 7.874, 'aluminum': 2.7, 'gold': 19.3, 'silver': 10.5}

    def calculate_weight(self, volume, material):
        if material not in self.densities:
            raise ValueError(f'Unsupported material: {material}')
        density = self.densities[material]
        weight = density * volume
        return weight
if __name__ == '__main__':
    calculator = MaterialCalculator()
    print(calculator.calculate_weight(1.0, 'iron'))
    print(calculator.calculate_weight(2.0, 'aluminum'))
    print(calculator.calculate_weight(0.5, 'gold'))
    print(calculator.calculate_weight(3.0, 'silver'))