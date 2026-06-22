def grams_to_ounces(weights):
    return [weight / 28.3495 for weight in weights]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)