def convert_to_ounces(weights):
    conversion_factors = {'kg': 35.274, 'lb': 16}
    ounces_list = [weight * conversion_factors[unit] for weight, unit in weights]
    return ounces_list

def combine_weights(ounces1, ounces2):
    combined_ounces = ounces1 + ounces2
    return combined_ounces

if __name__ == '__main__':
    weights_pounds = [(10, 'lb'), (5, 'lb')]
    weights_kilograms = [(2, 'kg'), (3, 'kg')]
    
    ounces_pounds = convert_to_ounces(weights_pounds)
    ounces_kilograms = convert_to_ounces(weights_kilograms)
    
    combined_weights = combine_weights(ounces_pounds, ounces_kilograms)
    
    print(combined_weights)