import numpy as np
def calculate_equivalent_weights(masses):
    if masses.size == 0:
        return np.array([])
    moles = masses / 100.0
    total_mass = np.sum(masses * moles)
    equivalent_weights = masses * moles / total_mass
    return equivalent_weights
if __name__ == '__main__':
    component_masses = np.array([10.0, 20.0, 30.0])
    weights = calculate_equivalent_weights(component_masses)
    print(weights)