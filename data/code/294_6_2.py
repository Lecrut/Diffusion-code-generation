import numpy as np
def calculate_equivalent_weights(masses):
    if masses.size == 0:
        return np.array([])
    total_mass = np.sum(masses)
    equivalent_weights = masses / total_mass
    return equivalent_weights
if __name__ == '__main__':
    component_masses = np.array([12.0, 16.0, 28.0, 36.0])
    weights = calculate_equivalent_weights(component_masses)
    print(weights)