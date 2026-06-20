def convert_kg_to_pounds(weights):
    return [weight * 2.20462 for weight in weights]

if __name__ == '__main__':
    sample_weights = [10, 20, 50, 100]
    results = convert_kg_to_pounds(sample_weights)
    for original, converted in zip(sample_weights, results):
        print(f"{original} kg is {converted:.2f} lbs")