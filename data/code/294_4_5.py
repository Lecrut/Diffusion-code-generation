def calculate_equivalent_weight(mass, molecular_weight):
    return mass * (molecular_weight / 100)

if __name__ == '__main__':
    sample_mass = 44.0
    sample_molecular_weight = 44.01
    equivalent_weight = calculate_equivalent_weight(sample_mass, sample_molecular_weight)
    print(equivalent_weight)