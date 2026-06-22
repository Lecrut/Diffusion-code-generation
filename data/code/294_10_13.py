def calculate_equivalent_weight(density, volume):
    return density * volume

if __name__ == '__main__':
    materials = {
        'wood': {'density': 0.6, 'volume': 1},
        'metal': {'density': 7.85, 'volume': 0.2}
    }
    
    for material, properties in materials.items():
        weight = calculate_equivalent_weight(properties['density'], properties['volume'])
        print(f"The equivalent weight of {material} is: {weight}")