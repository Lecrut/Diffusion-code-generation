CO2_MOLECULAR_WEIGHT = 44.01

def calculate_equivalent_weight(mass):
    return mass * (CO2_MOLECULAR_WEIGHT / 100)
if __name__ == '__main__':
    mass_sample = 44.0
    equivalent_weight = calculate_equivalent_weight(mass_sample)
    print(equivalent_weight)