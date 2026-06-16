import math
def calculate_equivalent_weight(component_weights, molecular_weights):
    total_equivalent_weight = 0
    for weight, mw in zip(component_weights, molecular_weights):
        equivalent_weight = weight * mw
        total_equivalent_weight += equivalent_weight
    return total_equivalent_weight
if __name__ == '__main__':
    component_weights = [10.0, 5.0]
    molecular_weights = [44.0, 18.0]
    equivalent_weight = calculate_equivalent_weight(component_weights, molecular_weights)
    print(equivalent_weight)