def calculate_equivalent_weight(mass, molecular_weight):
    return mass / molecular_weight

if __name__ == '__main__':
    water_mass = 18.0
    oxygen_atomic_mass = 16.0
    equivalent_water_weight = calculate_equivalent_weight(water_mass, 2 * oxygen_atomic_mass + 2)
    print(equivalent_water_weight)