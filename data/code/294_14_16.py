def calculate_equivalent_weights(materials):
    equivalent_weights = {}
    for material_id, material_data in materials.items():
        density = material_data.get('density')
        volume = material_data.get('volume')
        if density is None or volume is None:
            raise ValueError(f"Missing density or volume for material {material_id}")
        if density <= 0 or volume <= 0:
            raise ValueError(f"Invalid density or volume for material {material_id}")
        equivalent_weight = density * volume
        equivalent_weights[material_id] = equivalent_weight
    return equivalent_weights

if __name__ == '__main__':
    sample_materials = {
        "Material_A": {"density": 2.5, "volume": 10},
        "Material_B": {"density": 3.0, "volume": 5}
    }
    try:
        weights = calculate_equivalent_weights(sample_materials)
        print(weights)
    except ValueError as e:
        print(e)