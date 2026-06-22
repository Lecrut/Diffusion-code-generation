def convert_weights_to_ounces(weight_dict):
    if not weight_dict:
        return {}
    
    converted_dict = {}
    
    for item, weight in weight_dict.items():
        if isinstance(weight, dict):
            converted_dict[item] = convert_weights_to_ounces(weight)
        else:
            converted_dict[item] = weight * 35.274
    
    return converted_dict

if __name__ == '__main__':
    sample_dict = {
        'apple': 0.2,
        'banana': {'small': 0.1, 'large': 0.15},
        'orange': 0.18
    }
    
    result = convert_weights_to_ounces(sample_dict)
    print(result)