def grams_to_ounces(grams):
    ounces = [round(g * 0.035274, 2) for g in grams]
    return ounces

if __name__ == '__main__':
    weights_in_grams = [100, 250, 500, 750, 1000]
    weights_in_ounces = grams_to_ounces(weights_in_grams)
    print(weights_in_ounces)