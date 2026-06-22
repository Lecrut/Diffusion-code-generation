def grams_to_ounces(grams):
    ounces = [round(g * 0.035274, 2) for g in grams]
    return ounces

if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400, 500]
    print(grams_to_ounces(sample_weights))