def validate_inputs(materials):
    if not materials:
        raise ValueError("No materials provided")
    for material in materials:
        if 'density' not in material or 'volume' not in material:
            raise ValueError("Each material must have 'density' and 'volume' keys")

def calculate_equivalent_weights(materials):
    validate_inputs(materials)
    equivalent_weights = {}
    for material in materials:
        density = material['density']
        volume = material['volume']
        if density <= 0 or volume <= 0:
            equivalent_weight = None
        else:
            equivalent_weight = density * volume
        equivalent_weights[material['name']] = equivalent_weight
    return equivalent_weights

if __name__ == '__main__':
    sample_materials = [
        {'name': 'Material A', 'density': 1.2, 'volume': 0.5},
        {'name': 'Material B', 'density': 3.4, 'volume': 0.7},
        {'name': 'Material C', 'density': 0, 'volume': 0.8}
    ]
    weights = calculate_equivalent_weights(sample_materials)
    print(weights)