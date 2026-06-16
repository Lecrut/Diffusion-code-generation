import math
def calculate_equivalent_weight(component_weights, molecular_weights):
    total_equivalent_weight = 0
    for weight, mw in zip(component_weights, molecular_weights):
        equivalent_weight = weight * mw
        total_equivalent_weight += equivalent_weight
    return total_equivalent_weight
if __name__ == '__main__':
    component_weights = [1.5, 2.0, 3.5]
    molecular_weights = [40.0, 50.0, 60.0]
    result = calculate_equivalent_weight(component_weights, molecular_weights)
    print(result)