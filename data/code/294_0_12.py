def calculate_equivalent_weight(component_weights, molecular_weights):
    return sum(weight * mw for weight, mw in zip(component_weights, molecular_weights))

if __name__ == '__main__':
    component_weights = [10.0, 5.0]
    molecular_weights = [44.0, 18.0]
    result = calculate_equivalent_weight(component_weights, molecular_weights)
    print(result)