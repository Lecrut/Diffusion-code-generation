def calculate_equivalent_weight(mass, volume):
    if not (isinstance(mass, (int, float)) and isinstance(volume, (int, float))):
        raise ValueError("Both mass and volume must be numeric values.")
    
    density = mass / volume
    
    if density <= 0:
        raise ValueError("Density cannot be zero or negative.")
    
    return density

if __name__ == '__main__':
    mass_val = 100.0
    volume_val = 50.0
    equivalent_weight = calculate_equivalent_weight(mass_val, volume_val)
    print(equivalent_weight)