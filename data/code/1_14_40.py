def convert_kg_to_pounds(kg_list):
    return [kg * 2.20462 for kg in kg_list]

if __name__ == '__main__':
    sample_weights = [50, 75, 100, 150]
    converted_weights = convert_kg_to_pounds(sample_weights)
    print(converted_weights)