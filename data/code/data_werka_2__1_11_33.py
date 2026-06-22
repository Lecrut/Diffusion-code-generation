def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

if __name__ == '__main__':
    sample_weights_kg = [50, 70, 90, 110]
    converted_weights_lb = [kilograms_to_pounds(weight) for weight in sample_weights_kg]
    print(converted_weights_lb)