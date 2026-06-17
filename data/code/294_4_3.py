import math
def calculate_equivalent_weight(mass, molecular_weight):
    if molecular_weight == 0:
        return float('inf')
    return mass * (molecular_weight / 100.0)
if __name__ == '__main__':
    mass_sample = 10.5
    molecular_weight_sample = 18.035                        
    equivalent_weight = calculate_equivalent_weight(mass_sample, molecular_weight_sample)
    print(equivalent_weight)