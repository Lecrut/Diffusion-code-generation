OXYGEN_ATOMIC_MASS = 16
MOLECULAR_MASS_CAOH2 = 74.09

def calculate_equivalent_weight(mass):
    oxygen_mass = OXYGEN_ATOMIC_MASS * 2
    equivalent_weight = mass / (MOLECULAR_MASS_CAOH2 - oxygen_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 74
    result = calculate_equivalent_weight(sample_mass)
    print(result)