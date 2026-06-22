def grams_to_ounces(grams):
    conversion_factor = 0.035274
    return round(grams * conversion_factor, 4)

if __name__ == '__main__':
    initial_value = 1000
    result = grams_to_ounces(initial_value)
    print(result)