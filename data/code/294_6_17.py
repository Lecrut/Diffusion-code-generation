def calculate_equivalent_weight(mass_ammonia, mass_hydrogen):
    molar_mass_ammonia = 17.03
    molar_mass_hydrogen = 1.01
    equivalent_weight = (mass_ammonia / molar_mass_ammonia) + (mass_hydrogen / molar_mass_hydrogen)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass_ammonia = 17
    sample_mass_hydrogen = 2
    result = calculate_equivalent_weight(sample_mass_ammonia, sample_mass_hydrogen)
    print(result)