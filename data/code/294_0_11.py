def validate_input(component_weights, molecular_weights):
    if not all(isinstance(x, (int, float)) for x in component_weights + molecular_weights):
        raise ValueError("All weights and molar masses must be numbers.")
    if len(component_weights) != len(molecular_weights):
        raise ValueError("Component weights and molecular weights must have the same length.")

def calculate_equivalent_weight(component_weights, molecular_weights):
    validate_input(component_weights, molecular_weights)
    total_equivalent_weight = sum(weight * mw for weight, mw in zip(component_weights, molecular_weights))
    return total_equivalent_weight

if __name__ == '__main__':
    component_weights = [10.0, 5.0]
    molecular_weights = [44.0, 18.0]
    equivalent_weight = calculate_equivalent_weight(component_weights, molecular_weights)
    print(equivalent_weight)