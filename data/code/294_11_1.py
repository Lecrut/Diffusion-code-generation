import numpy as np
def calculate_equivalent_weight(mass, moles, atomic_weight):
    if not isinstance(mass, (np.ndarray, float)) or not isinstance(moles, (np.ndarray, float)) or not isinstance(atomic_weight, (np.ndarray, float)):
        raise TypeError("Inputs must be numeric or numpy arrays.")
    if np.isscalar(mass) and np.isscalar(moles) and np.isscalar(atomic_weight):
        equivalent_weight = mass / moles * atomic_weight
        return equivalent_weight
    else:
        result = mass / moles * atomic_weight
        return result
if __name__ == '__main__':
    mass_val = 10.0
    moles_val = 2.5
    atomic_weight_val = 44.0
    single_result = calculate_equivalent_weight(mass_val, moles_val, atomic_weight_val)
    print(f"Single result: {single_result}")
    mass_array = np.array([10.0, 20.0, 30.0])
    moles_array = np.array([2.5, 5.0, 7.5])
    atomic_weight_array = np.array([44.0, 44.0, 44.0])
    vectorized_result = calculate_equivalent_weight(mass_array, moles_array, atomic_weight_array)
    print(f"Vectorized result: {vectorized_result}")