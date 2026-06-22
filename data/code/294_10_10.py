def calculate_equivalent_weights(materials):
    if not isinstance(materials, dict):
        raise ValueError("Input must be a dictionary.")
    
    equivalent_weights = {}
    for material, (density, volume) in materials.items():
        if not all(isinstance(x, (int, float)) for x in [density, volume]):
            raise ValueError(f"Invalid values for material {material}.")
        weight = density * volume
        equivalent_weights[material] = weight
    
    return equivalent_weights

if __name__ == '__main__':
    sample_materials = {
        'iron': (7.874, 0.5),
        'aluminum': (2.7, 1.0),
        'gold': (19.3, 0.2)
    }
    
    try:
        weights = calculate_equivalent_weights(sample_materials)
        print(weights)
    except ValueError as e:
        print(e)