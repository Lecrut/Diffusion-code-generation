MOLAR_MASS_BACL2 = 207.2
ATOMIC_MASS_CL = 35.45

def calculate_equivalent_weight(mass_bacl2):
    equivalent_weight = mass_bacl2 / (MOLAR_MASS_BACL2 - 2 * ATOMIC_MASS_CL)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 207
    result = calculate_equivalent_weight(sample_mass)
    print(result)