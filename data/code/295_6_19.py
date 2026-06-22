GRAMS_TO_OUNCES = 0.035274

def grams_to_ounces(grams):
    return round(grams * GRAMS_TO_OUNCES, 4)

if __name__ == '__main__':
    sample_value = 160
    result = grams_to_ounces(sample_value)
    print(result)