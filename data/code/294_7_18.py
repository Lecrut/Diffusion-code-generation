def calculate_equivalent_weight(mass, molar_mass):
    return mass / molar_mass

if __name__ == '__main__':
    sulfuric_acid_mass = 98.0
    oxygen_atomic_mass = 16.0
    equivalent_weight_oxygen = calculate_equivalent_weight(sulfuric_acid_mass * 4, oxygen_atomic_mass * 4)
    print(equivalent_weight_oxygen)