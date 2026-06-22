def calculate_equivalent_weight(mass_bacl2):
    molar_mass_bacl2 = 207.2
    atomic_mass_cl = 35.45
    return mass_bacl2 / (molar_mass_bacl2 - 2 * atomic_mass_cl)

if __name__ == '__main__':
    sample_mass = 207
    print(calculate_equivalent_weight(sample_mass))