import numpy as np
def calculate_equivalent_weight(mass, moles, atomic_weight):
    if np.isscalar(mass) and np.isscalar(moles) and np.isscalar(atomic_weight):
        return mass / moles * atomic_weight
    else:
        result = mass / moles * atomic_weight
        return result
if __name__ == '__main__':
    mass_val = 100.0
    moles_val = 2.5
    atomic_weight_val = 50.0
    equivalent_weight = calculate_equivalent_weight(mass_val, moles_val, atomic_weight_val)
    print(equivalent_weight)
    mass_array = np.array([100.0, 200.0, 300.0])
    moles_array = np.array([2.5, 5.0, 7.5])
    atomic_weight_array = np.array([50.0, 50.0, 50.0])
    equivalent_weights_array = calculate_equivalent_weight(mass_array, moles_array, atomic_weight_array)
    print(equivalent_weights_array)