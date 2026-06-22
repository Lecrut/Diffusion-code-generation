def calculate_equivalent_weight(mass):
    molar_mass = 74.09
    oxygen_atomic_mass = 16
    if mass <= 0:
        raise ValueError("Mass must be greater than zero")
    equivalent_weight = mass / (molar_mass - 2 * oxygen_atomic_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 74
    try:
        result = calculate_equivalent_weight(sample_mass)
        print(result)
    except ValueError as e:
        print(e)