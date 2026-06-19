def kg_to_pounds(weights_kg):
    return [weight * 2.20462 for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [50, 70, 90, 110]
    converted_weights = kg_to_pounds(sample_weights)
    print(converted_weights)