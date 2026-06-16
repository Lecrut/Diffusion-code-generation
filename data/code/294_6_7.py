import numpy as np
def calculate_equivalent_weights(masses):
    if masses.size == 0:
        return np.array([])
    moles = masses / 100.0
    total_mass = np.sum(masses)
    weights = moles / total_mass
    return weights
if __name__ == '__main__':
    component_masses = np.array([10.0, 20.0, 30.0])
    equivalent_weights = calculate_equivalent_weights(component_masses)
    print(equivalent_weights)