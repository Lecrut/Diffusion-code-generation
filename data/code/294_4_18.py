MOLECULAR_WEIGHT_CO2 = 44.01
ATOMIC_MASS_OXYGEN = 16.0

def calculate_equivalent_weight(mass, molecular_weight):
    if molecular_weight == 0:
        return float('inf')
    return mass * (molecular_weight / 100.0)
if __name__ == '__main__':
    mass_sample = 44.0
    equivalent_weight = calculate_equivalent_weight(mass_sample, MOLECULAR_WEIGHT_CO2)
    print(equivalent_weight)