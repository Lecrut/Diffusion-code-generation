def grams_to_ounces(grams):
    if not isinstance(grams, (int, float)):
        raise ValueError("Input must be a number.")
    return round(grams * 0.035274, 4)

if __name__ == '__main__':
    sample_value = 160
    result = grams_to_ounces(sample_value)
    print(result)