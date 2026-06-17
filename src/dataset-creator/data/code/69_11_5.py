def grams_to_kilograms(grams: float) -> float:
    return grams / 1000
if __name__ == '__main__':
    sample_mass = 2500.0
    result = grams_to_kilograms(sample_mass)
    print(f"{sample_mass} g is equal to {result:.4f} kg")