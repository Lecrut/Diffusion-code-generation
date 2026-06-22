def calculate_equivalent_weight(mass, molecular_weight):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero")
    if molecular_weight <= 0:
        raise ValueError("Molecular weight must be greater than zero")
    return mass / molecular_weight

if __name__ == '__main__':
    mass_sample = 44.0
    molecular_weight_sample = 44.01
    equivalent_weight = calculate_equivalent_weight(mass_sample, molecular_weight_sample)
    print(equivalent_weight)