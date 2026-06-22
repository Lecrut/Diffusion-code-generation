conversion_factors = {
    'g_to_oz': 0.035274
}

def grams_to_ounces(grams: list) -> list:
    return [round(g * conversion_factors['g_to_oz'], 2) for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 250, 300]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)