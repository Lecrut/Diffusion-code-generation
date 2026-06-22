def calculate_equivalent_weight(mass):
    molar_mass = 18.015
    oxygen_atomic_mass = 16
    equivalent_weight = mass / (molar_mass - oxygen_atomic_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 18
    result = calculate_equivalent_weight(sample_mass)
    print(result)