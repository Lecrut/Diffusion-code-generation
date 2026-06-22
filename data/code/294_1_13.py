def calculate_equivalent_weight(mass, molecular_weight):
    if mass <= 0 or molecular_weight <= 0:
        raise ValueError("Mass and molecular weight must be positive values")
    return mass / molecular_weight

if __name__ == '__main__':
    water_mass = 18.0
    oxygen_atomic_mass = 16.0
    equivalent_weight = calculate_equivalent_weight(water_mass, oxygen_atomic_mass)
    print(equivalent_weight)