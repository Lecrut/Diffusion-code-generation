def calculate_equivalent_weight(densities, quantities):
    return {substance: density * quantity for substance, (density, quantity) in zip(substances, quantities)}
if __name__ == '__main__':
    substances = ['water', 'alcohol', 'oil']
    densities = [1000, 800, 920]
    quantities = [(1, 'L'), (0.5, 'L'), (2, 'L')]
    weights = calculate_equivalent_weight(densities, quantities)
    print(weights)