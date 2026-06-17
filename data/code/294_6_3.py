import numpy as np
def calculate_equivalent_weights(masses):
    if masses.ndim == 1:
        total_mass = np.sum(masses)
        weights = masses / total_mass
        return weights
    else:
        total_mass = np.sum(masses, axis=0)
        weights = masses / total_mass
        return weights
if __name__ == '__main__':
    component_masses = np.array([12.011, 16.000, 1.008])
    equivalent_weights = calculate_equivalent_weights(component_masses)
    print(equivalent_weights)