def grams_to_kilograms(mass_in_grams: float) -> float:
    return mass_in_grams / 1000
if __name__ == '__main__':
    sample_mass = 2500
    result = grams_to_kilograms(sample_mass)
    print(result)