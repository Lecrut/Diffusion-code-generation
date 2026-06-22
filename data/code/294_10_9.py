def calculate_equivalent_weight(density, volume):
    return density * volume

if __name__ == '__main__':
    materials = {
        'Aluminum': {'density': 2.7, 'volume': 100},
        'Steel': {'density': 7.85, 'volume': 50},
        'Plastic': {'density': 1.2, 'volume': 150}
    }
    
    for material, properties in materials.items():
        weight = calculate_equivalent_weight(properties['density'], properties['volume'])
        print(f"The equivalent weight of {material} is: {weight}")