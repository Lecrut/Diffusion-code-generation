def pounds_to_ounces(pounds):
    return pounds * 16

def kilograms_to_ounces(kilograms):
    return kilograms * 35.274

def validate_weights(weights, units):
    if len(weights) != len(units):
        raise ValueError("Weights and units lists must be of the same length")
    if any(not isinstance(w, (int, float)) for w in weights):
        raise ValueError("All weights must be numbers")
    if any(u not in ['lb', 'kg'] for u in units):
        raise ValueError("Units must be either 'lb' or 'kg'")

def combine_weights(weights_pounds, weights_kilograms):
    validate_weights(weights_pounds, ['lb'] * len(weights_pounds))
    validate_weights(weights_kilograms, ['kg'] * len(weights_kilograms))
    
    ounces_pounds = [pounds_to_ounces(w) for w in weights_pounds]
    ounces_kilograms = [kilograms_to_ounces(w) for w in weights_kilograms]
    
    combined_ounces = ounces_pounds + ounces_kilograms
    return combined_ounces

if __name__ == '__main__':
    weights_pounds = [10, 20, 30]
    weights_kilograms = [5, 7.5]
    print(combine_weights(weights_pounds, weights_kilograms))