def convert_kg_to_lbs(weights_kg):
    return [kg * 2.20462 for kg in weights_kg]
if __name__ == '__main__':
    sample_weights_kg = [0, 50, 70, 90, 120]
    converted_weights_lbs = convert_kg_to_lbs(sample_weights_kg)
    print(converted_weights_lbs)