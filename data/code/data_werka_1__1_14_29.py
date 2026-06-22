def kg_to_pounds(kg_values):
    return [kg * 2.20462 for kg in kg_values]

if __name__ == '__main__':
    sample_weights_kg = [50, 75, 100, 120]
    converted_weights = kg_to_pounds(sample_weights_kg)
    print(converted_weights)