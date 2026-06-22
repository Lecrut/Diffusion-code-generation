def grams_to_ounces(grams):
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300]
    weights_in_ounces = grams_to_ounces(weights_in_grams)
    print(weights_in_ounces)