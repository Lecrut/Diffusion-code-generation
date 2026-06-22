def calculate_equivalent_weight(component_weights, molecular_weights):
    if not component_weights or not molecular_weights:
        raise ValueError("Both component weights and molecular weights must be non-empty lists.")
    if len(component_weights) != len(molecular_weights):
        raise ValueError("Component weights and molecular weights must have the same length.")
    
    total_equivalent_weight = 0.0
    for weight, mw in zip(component_weights, molecular_weights):
        if not isinstance(weight, (int, float)) or not isinstance(mw, (int, float)):
            raise TypeError("Both component weights and molecular weights must contain numbers.")
        if weight < 0 or mw <= 0:
            raise ValueError("Component weights must be non-negative and molecular weights must be positive.")
        
        equivalent_weight = weight * mw
        total_equivalent_weight += equivalent_weight
    
    return total_equivalent_weight

if __name__ == '__main__':
    component_weights = [10.0, 5.0]
    molecular_weights = [44.0, 18.0]
    result = calculate_equivalent_weight(component_weights, molecular_weights)
    print(result)