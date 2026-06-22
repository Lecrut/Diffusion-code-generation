CONVERSION_FACTORS = {
    ('gram', 'ounce'): 0.035274
}

def grams_to_ounces(grams):
    return round(grams * CONVERSION_FACTORS[('gram', 'ounce')], 4)

if __name__ == '__main__':
    sample_value = 160
    result = grams_to_ounces(sample_value)
    print(result)