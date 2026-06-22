def calculate_equivalent_weight(mass, molecular_weight):
    if mass <= 0 or molecular_weight <= 0:
        raise ValueError("Mass and molecular weight must be positive numbers.")
    
    return mass * (molecular_weight / 100.0)

if __name__ == '__main__':
    try:
        mass_sample = 44.0
        molecular_weight_sample = 44.01
        equivalent_weight = calculate_equivalent_weight(mass_sample, molecular_weight_sample)
        print(equivalent_weight)
    except ValueError as e:
        print(e)