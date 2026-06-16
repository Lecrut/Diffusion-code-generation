import math
def calculate_equivalent_weight(masses, molecular_weights):
    total_equivalent_weight = 0.0
    for mass, mw in zip(masses, molecular_weights):
        if mw != 0:
            equivalent_weight = mass / mw
            total_equivalent_weight += equivalent_weight
    return total_equivalent_weight
if __name__ == '__main__':
    component_masses = [10.0, 5.0, 20.0]
    molecular_weights = [18.015, 39.047, 44.01]
    result = calculate_equivalent_weight(component_masses, molecular_weights)
    print(result)