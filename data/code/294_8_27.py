def calculate_molar_mass_bacl2():
    return 207.2

def calculate_atomic_mass_cl():
    return 35.45

def calculate_equivalent_weight(mass_bacl2):
    molar_mass_bacl2 = calculate_molar_mass_bacl2()
    atomic_mass_cl = calculate_atomic_mass_cl()
    equivalent_weight = mass_bacl2 / (molar_mass_bacl2 - 2 * atomic_mass_cl)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass_bacl2 = 207
    result = calculate_equivalent_weight(sample_mass_bacl2)
    print(result)