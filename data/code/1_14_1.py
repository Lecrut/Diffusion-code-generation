KG_TO_LB_CONVERSION_FACTOR = 2.20462

def convert_kg_to_lb(kg):
    return kg * KG_TO_LB_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_weights_kg = [10.0, 50.5, 100.0, 75.25, 0.5]
    converted_weights = [convert_kg_to_lb(weight) for weight in sample_weights_kg]
    print(converted_weights)