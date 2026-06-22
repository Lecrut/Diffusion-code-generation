def grams_to_ounces(weights):
    ounces = [weight / 28.3495 for weight in weights]
    return ounces

if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400, 500]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)