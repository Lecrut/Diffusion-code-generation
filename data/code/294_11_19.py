def calculate_equivalent_weight(mass, volume):
    density = mass / volume
    return density

if __name__ == '__main__':
    mass_val = 100.0
    volume_val = 25.0
    equivalent_weight = calculate_equivalent_weight(mass_val, volume_val)
    print(equivalent_weight)