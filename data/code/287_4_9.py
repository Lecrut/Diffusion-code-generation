def convert_to_ounces(weights):
    ounces = []
    for weight, unit in weights:
        if unit == 'lb':
            ounces.append(weight * 16)
        elif unit == 'kg':
            ounces.append(weight * 35.274)
        else:
            raise ValueError(f"Unsupported unit: {unit}")
    return ounces

def combine_weights(pounds, kilograms):
    pounds_ounces = convert_to_ounces(pounds)
    kilograms_ounces = convert_to_ounces(kilograms)
    combined_ounces = pounds_ounces + kilograms_ounces
    return combined_ounces

if __name__ == '__main__':
    sample_pounds = [('10', 'lb'), ('5', 'lb')]
    sample_kilograms = [('2', 'kg'), ('3', 'kg')]
    result = combine_weights(sample_pounds, sample_kilograms)
    print(result)