def convert_to_ounces(weights):
    conversion_factors = {'kg': 35.274, 'lb': 16}
    ounces_list = []
    for weight in weights:
        value, unit = weight.split()
        try:
            value = float(value)
            unit = unit.strip('kglb')
        except ValueError:
            raise ValueError("Invalid weight format")
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        ounces_list.append(value * conversion_factors[unit])
    return ounces_list

def combine_weights(list1, list2):
    ounces_list1 = convert_to_ounces(list1)
    ounces_list2 = convert_to_ounces(list2)
    combined_list = [w1 + w2 for w1, w2 in zip(ounces_list1, ounces_list2)]
    return combined_list

if __name__ == '__main__':
    list1 = ['5 kg', '3 lb']
    list2 = ['2 kg', '4 lb']
    result = combine_weights(list1, list2)
    print(result)