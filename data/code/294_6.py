import numpy as np
def calculate_equivalent_weights(masses):
    if masses.size == 0:
        return np.array([])
    total_mass = np.sum(masses)
    weights = masses / total_mass
    return weights
if __name__ == '__main__':
    component_masses = np.array([12.011, 16.000, 1.008, 18.015])
    equivalent_weights = calculate_equivalent_weights(component_masses)
    print(equivalent_weights)