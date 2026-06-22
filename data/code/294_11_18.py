def calculate_equivalent_weight(mass, volume, density):
    return mass / volume * density

if __name__ == '__main__':
    mass_val = 150.0
    volume_val = 3.0
    density_val = 50.0
    equivalent_weight = calculate_equivalent_weight(mass_val, volume_val, density_val)
    print(equivalent_weight)