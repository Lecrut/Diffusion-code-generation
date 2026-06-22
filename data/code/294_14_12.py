def calculate_equivalent_weights(materials):
    equivalent_weights = {}
    for material_id, data in materials.items():
        density = data.get('density')
        volume = data.get('volume')
        if density is None or volume is None:
            raise ValueError(f"Missing density or volume for material {material_id}")
        if density <= 0 or volume <= 0:
            raise ValueError(f"Invalid density or volume for material {material_id}")
        equivalent_weight = density * volume
        equivalent_weights[material_id] = equivalent_weight
    return equivalent_weights

if __name__ == '__main__':
    sample_materials = {
        "M1": {"density": 2.7, "volume": 10},
        "M2": {"density": 5.8, "volume": 5}
    }
    print(calculate_equivalent_weights(sample_materials))