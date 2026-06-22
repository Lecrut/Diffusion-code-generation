def calculate_equivalent_weight(densities, quantities):
    return {substance: density * quantity for substance, (density, quantity) in zip(substances, quantities)}
if __name__ == '__main__':
    substances = ['Substance A', 'Substance B', 'Substance C']
    densities = [2.5, 3.0, 1.8]
    quantities = [(100, 'cm^3'), (200, 'cm^3'), (150, 'cm^3')]
    results = calculate_equivalent_weight(densities, quantities)
    print(results)