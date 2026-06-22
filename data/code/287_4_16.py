def convert_to_ounces(weight_list):
    ounces_list = []
    for weight in weight_list:
        value, unit = weight.split()
        value = float(value)
        if unit == 'lb':
            ounces = value * 16
        elif unit == 'kg':
            ounces = value * 35.274
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        ounces_list.append(ounces)
    return ounces_list

def combine_weights(pounds, kilograms):
    pounds_ounces = convert_to_ounces(pounds)
    kilograms_ounces = convert_to_ounces(kilograms)
    combined_ounces = pounds_ounces + kilograms_ounces
    return combined_ounces

if __name__ == '__main__':
    pounds_weights = ['10 lb', '20 lb']
    kilograms_weights = ['5 kg', '3 kg']
    combined_weights = combine_weights(pounds_weights, kilograms_weights)
    print(combined_weights)