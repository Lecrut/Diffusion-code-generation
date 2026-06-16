import numpy as np
def calculate_equivalent_weights(masses):
    if masses.ndim == 1:
        moles = np.ones_like(masses)
        total_mass = np.sum(masses * moles)
        equivalent_weights = masses / total_mass
        return equivalent_weights
    else:
        raise ValueError("Input must be a 1D array of masses.")
if __name__ == '__main__':
    component_masses = np.array([10.0, 20.0, 30.0])
    equivalent_weights = calculate_equivalent_weights(component_masses)
    print(equivalent_weights)