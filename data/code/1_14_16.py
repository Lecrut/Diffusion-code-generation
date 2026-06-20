def kilograms_to_pounds(kg_values):
    return [kg * 2.20462 for kg in kg_values]

if __name__ == '__main__':
    sample_weights = [0, 1, 5, 10, 50, 100, 123.456]
    result = kilograms_to_pounds(sample_weights)
    print(result)