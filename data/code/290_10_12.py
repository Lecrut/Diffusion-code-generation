def convert_grams_to_ounces(grams):
    if not isinstance(grams, (int, float)):
        raise ValueError("Input must be a number.")
    return grams / 28.3495

if __name__ == '__main__':
    sample_mass = 1000
    result = convert_grams_to_ounces(sample_mass)
    print(f"Converted Mass: {result} ounces")