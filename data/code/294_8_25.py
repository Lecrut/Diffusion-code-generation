def calculate_equivalent_weight(mass_bacl2):
    molar_mass_bacl2 = 207.2
    atomic_mass_cl = 35.45

    if mass_bacl2 <= 0:
        raise ValueError("Mass must be greater than zero.")

    equivalent_weight = mass_bacl2 / (molar_mass_bacl2 - 2 * atomic_mass_cl)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 207
    result = calculate_equivalent_weight(sample_mass)
    print(result)