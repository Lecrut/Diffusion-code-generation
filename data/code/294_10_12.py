def validate_density_and_volume(density, volume):
    if not isinstance(density, (int, float)) or density <= 0:
        raise ValueError("Density must be a positive number")
    if not isinstance(volume, (int, float)) or volume <= 0:
        raise ValueError("Volume must be a positive number")

def calculate_weight(density, volume):
    validate_density_and_volume(density, volume)
    return density * volume

if __name__ == '__main__':
    material_data = {
        'Steel': {'density': 7850, 'volume': 0.1},
        'Aluminum': {'density': 2700, 'volume': 0.2}
    }
    
    for material, properties in material_data.items():
        weight = calculate_weight(properties['density'], properties['volume'])
        print(f"The equivalent weight of {material} is: {weight}")