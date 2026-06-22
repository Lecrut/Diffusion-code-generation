def calculate_equivalent_weight(densities, quantities):
    return {substance: density * quantity for substance, (density, quantity) in zip(substances, quantities)}
if __name__ == '__main__':
    substances = ['Water', 'Ethanol']
    densities = [1000, 789.8]
    quantities = [(1, 'L'), (0.5, 'L')]
    print(calculate_equivalent_weight(substances, densities))