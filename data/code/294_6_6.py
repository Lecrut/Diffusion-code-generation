import numpy as np
def calculate_equivalent_weights(masses):
    if masses.ndim == 1:
        n = len(masses)
        weights = np.zeros_like(masses, dtype=float)
        if n > 0:
            weights[0] = masses[0]
            for i in range(1, n):
                weights[i] = masses[i] / masses[0]
        return weights
    else:
        raise ValueError("Input must be a 1D array.")
if __name__ == '__main__':
    component_masses = np.array([12.011, 16.000, 18.015, 28.050])
    equivalent_weights = calculate_equivalent_weights(component_masses)
    print(equivalent_weights)