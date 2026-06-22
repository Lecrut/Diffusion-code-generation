def pounds_to_ounces(pounds):
    return pounds * 16

def kilograms_to_ounces(kilograms):
    return kilograms * 35.274

def convert_weights(weights, units):
    if len(weights) != len(units):
        raise ValueError("Weights and units lists must be of the same length")
    
    ounces = []
    for weight, unit in zip(weights, units):
        weight = float(weight)
        if unit == 'lb':
            ounces.append(pounds_to_ounces(weight))
        elif unit == 'kg':
            ounces.append(kilograms_to_ounces(weight))
        else:
            raise ValueError(f"Unsupported unit: {unit}")
    
    return ounces

def combine_weights(ounces1, ounces2):
    return [o1 + o2 for o1, o2 in zip(ounces1, ounces2)]

if __name__ == '__main__':
    weights_lb = ['10', '5']
    units_lb = ['lb', 'lb']
    
    weights_kg = ['2', '3']
    units_kg = ['kg', 'kg']
    
    ounces1 = convert_weights(weights_lb, units_lb)
    ounces2 = convert_weights(weights_kg, units_kg)
    
    combined_ounces = combine_weights(ounces1, ounces2)
    
    print(combined_ounces)