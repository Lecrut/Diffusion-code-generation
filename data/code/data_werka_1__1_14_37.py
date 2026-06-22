def kilograms_to_pounds(kg):
    return kg * 2.20462

if __name__ == '__main__':
    sample_weights_kg = [50, 75, 100, 150]
    converted_weights = [kilograms_to_pounds(weight) for weight in sample_weights_kg]
    print(converted_weights)