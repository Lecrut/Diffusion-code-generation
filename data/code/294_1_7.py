def calculate_equivalent_weight(mass, molecular_weight):
    return mass / molecular_weight
if __name__ == '__main__':
    water_mass = 18.0
    oxygen_atomic_mass = 16.0
    hydrogen_atomic_mass = 1.008
    molecular_weight_H2O = 2 * hydrogen_atomic_mass + oxygen_atomic_mass
    equivalent_weight = calculate_equivalent_weight(water_mass, molecular_weight_H2O)
    print(equivalent_weight)