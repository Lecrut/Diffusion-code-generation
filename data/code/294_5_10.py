def calculate_equivalent_weight(mass, molar_mass):
    if molar_mass <= 0:
        raise ValueError('Molar mass must be greater than zero')
    return mass / molar_mass
if __name__ == '__main__':
    try:
        methane_mass = 16.0
        carbon_mass = 12.0
        methane_molar_mass = 16.04
        carbon_molar_mass = 12.01
        equivalent_weight_methane = calculate_equivalent_weight(methane_mass, methane_molar_mass)
        equivalent_weight_carbon = calculate_equivalent_weight(carbon_mass, carbon_molar_mass)
        print(f'Equivalent weight of methane: {equivalent_weight_methane:.2f} mol')
        print(f'Equivalent weight of carbon: {equivalent_weight_carbon:.2f} mol')
    except ValueError as e:
        print(f'Error: {e}')