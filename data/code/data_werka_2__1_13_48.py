KG_TO_LB_CONVERSION_FACTOR = 2.20462

def convert_weights_to_pounds(weights_kg):
    def weight_converter(weight_kg):
        return weight_kg * KG_TO_LB_CONVERSION_FACTOR
    
    return [weight_converter(weight) for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1, 5, 10, 20]
    converted_weights = convert_weights_to_pounds(sample_weights)
    print(converted_weights)