GRAMS_TO_OUNCES = 28.3495

def grams_to_ounces(grams):
    return [g / GRAMS_TO_OUNCES for g in grams]

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300, 400]
    weights_in_ounces = grams_to_ounces(weights_in_grams)
    print(weights_in_ounces)