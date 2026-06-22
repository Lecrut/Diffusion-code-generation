def calculate_equivalent_weights(materials):
    density_volume_map = {
        "Water": {"density": 1000, "volume": 1},
        "Steel": {"density": 7850, "volume": 0.02},
        "Aluminum": {"density": 2700, "volume": 0.03}
    }
    equivalent_weights = {}
    for material, data in materials.items():
        density = density_volume_map.get(material, {}).get("density", 1)
        volume = density_volume_map.get(material, {}).get("volume", 1)
        if density > 0 and volume > 0:
            equivalent_weight = density * volume
        else:
            equivalent_weight = None
        equivalent_weights[material] = equivalent_weight
    return equivalent_weights

if __name__ == '__main__':
    sample_materials = {
        "Water": {},
        "Steel": {},
        "Aluminum": {}
    }
    results = calculate_equivalent_weights(sample_materials)
    print(results)