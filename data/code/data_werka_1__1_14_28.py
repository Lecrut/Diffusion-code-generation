def kilograms_to_pounds(weights):
    return [weight * 2.20462 for weight in weights]

if __name__ == '__main__':
    sample_weights = [50, 75, 100, 125]
    converted_weights = kilograms_to_pounds(sample_weights)
    print(converted_weights)