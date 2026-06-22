def grams_to_ounces(grams):
    if not isinstance(grams, (int, float)) or grams < 0:
        raise ValueError("Input must be a non-negative number representing grams.")
    
    conversion_factor = 0.035274
    ounces = grams * conversion_factor
    return round(ounces, 4)

if __name__ == '__main__':
    initial_value = 100
    result = grams_to_ounces(initial_value)
    print(result)