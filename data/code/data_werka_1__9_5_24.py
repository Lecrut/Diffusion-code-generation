def convert_volume_to_liters(volume, unit):
    conversion_factors = {
        'm³': 1000,
        'cm³': 0.001,
        'dm³': 1,
        'mm³': 0.000001,
        'in³': 0.016387064,
        'ft³': 28.316846592,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 0.0295735295625
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_volumes = [
        (1, 'm³'),
        (1000, 'cm³'),
        (2, 'dm³'),
        (1e9, 'mm³'),
        (1, 'in³'),
        (1, 'ft³'),
        (1, 'gal'),
        (1, 'qt'),
        (1, 'pt'),
        (8, 'fl oz')
    ]
    
    for volume, unit in sample_volumes:
        liters = convert_volume_to_liters(volume, unit)
        print(f"{volume} {unit} is equal to {liters} liters")