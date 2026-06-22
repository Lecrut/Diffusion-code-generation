def validate_material(material):
    if not material or 'density' not in material or 'volume' not in material:
        raise ValueError("Invalid material data")

def calculate_equivalent_weight(material):
    validate_material(material)
    density = material['density']
    volume = material['volume']
    return density * volume

if __name__ == '__main__':
    materials = [
        {"density": 2.7, "volume": 10},
        {"density": 5.9, "volume": 3},
        {"density": 8.9, "volume": 4}
    ]
    
    for material in materials:
        print(calculate_equivalent_weight(material))