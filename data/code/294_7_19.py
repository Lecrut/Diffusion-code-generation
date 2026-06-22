def calculate_equivalent_weight(mass):
    molar_mass = 98.08
    oxygen_atomic_mass = 16
    number_of_oxygen_atoms = 4
    equivalent_weight = (mass / molar_mass) * number_of_oxygen_atoms
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 98
    result = calculate_equivalent_weight(sample_mass)
    print(result)