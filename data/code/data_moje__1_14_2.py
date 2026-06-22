def kilograms_to_pounds(kg_values):
    return [kg * 2.20462 for kg in kg_values]

if __name__ == '__main__':
    sample_weights_kg = [1.0, 2.5, 5.0, 10.0, 50.0, 100.0]
    print(kilograms_to_pounds(sample_weights_kg))