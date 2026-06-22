def kilograms_to_pounds(kilograms_list):
    return [kg * 2.20462 for kg in kilograms_list]
if __name__ == '__main__':
    sample_weights_kg = [50, 60, 70, 80, 90, 100]
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)