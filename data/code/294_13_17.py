CONVERSION_FACTOR = 1000

def calculate_equivalent_weight(mass, volume):
    return mass / (volume * CONVERSION_FACTOR)

if __name__ == '__main__':
    sample_mass = 50.0
    sample_volume = 2.5
    print(calculate_equivalent_weight(sample_mass, sample_volume))