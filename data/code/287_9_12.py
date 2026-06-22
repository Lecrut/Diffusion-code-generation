KG_TO_OZ = 35.274

def convert_weights_to_ounces(weights_dict):
    if isinstance(weights_dict, dict):
        return {key: convert_weights_to_ounces(value) for key, value in weights_dict.items()}
    else:
        return weights_dict * KG_TO_OZ
if __name__ == '__main__':
    sample_data = {'apple': 0.5, 'banana': 0.2, 'box': {'grape': 0.1}}
    converted_data = convert_weights_to_ounces(sample_data)
    print(converted_data)