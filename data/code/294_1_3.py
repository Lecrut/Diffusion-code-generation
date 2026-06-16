def calculate_equivalent_weight(component_masses, molecular_weights):
    total_equivalent_weight = 0.0
    for mass, mw in zip(component_masses, molecular_weights):
        if mw != 0:
            equivalent_weight = mass / mw
            total_equivalent_weight += equivalent_weight
    return total_equivalent_weight
if __name__ == '__main__':
    component_masses_sample = [10.0, 5.0, 2.0]
    molecular_weights_sample = [18.015, 32.06, 16.00]
    result = calculate_equivalent_weight(component_masses_sample, molecular_weights_sample)
    print(result)