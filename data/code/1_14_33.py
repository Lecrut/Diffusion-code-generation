def kilograms_to_pounds(kilograms):
    return [kg * 2.20462 for kg in kilograms]

if __name__ == '__main__':
    sample_weights_kg = [1, 5, 10, 20, 50]
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)