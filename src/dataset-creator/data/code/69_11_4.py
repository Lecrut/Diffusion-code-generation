def grams_to_kilograms(grams: float) -> float:
    return grams / 1000
if __name__ == '__main__':
    mass_grams = 500
    result_kg = grams_to_kilograms(mass_grams)
    print(result_kg)