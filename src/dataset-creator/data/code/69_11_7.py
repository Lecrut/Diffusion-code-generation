def grams_to_kilograms(mass_grams: float) -> float:
    return mass_grams / 1000
if __name__ == '__main__':
    sample_mass = 500.0
    result = grams_to_kilograms(sample_mass)
    print(result)