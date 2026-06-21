CONVERSION_TABLE = {
    'kg_to_lb': 2.20462
}

def convert_weight(weight_kg):
    return weight_kg * CONVERSION_TABLE['kg_to_lb']

if __name__ == '__main__':
    sample_weights_kg = [30, 55, 80, 105]
    converted_weights_lb = [convert_weight(weight) for weight in sample_weights_kg]
    print(converted_weights_lb)