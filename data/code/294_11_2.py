import numpy as np
def calculate_equivalent_weight(mass, moles, atomic_weight):
    if not isinstance(mass, (np.ndarray, float)) or not isinstance(moles, (np.ndarray, float)) or not isinstance(atomic_weight, (np.ndarray, float)):
        raise TypeError("Inputs must be numeric or numpy arrays.")
    result = mass / moles * atomic_weight
    return result
if __name__ == '__main__':
    mass_val = 100.0
    moles_val = 2.5
    atomic_weight_val = 50.0
    result_scalar = calculate_equivalent_weight(mass_val, moles_val, atomic_weight_val)
    print(f"Scalar result: {result_scalar}")
    mass_array = np.array([100.0, 200.0, 300.0])
    moles_array = np.array([2.5, 5.0, 7.5])
    atomic_weight_array = np.array([50.0, 50.0, 50.0])
    result_vector = calculate_equivalent_weight(mass_array, moles_array, atomic_weight_array)
    print(f"Vector result: {result_vector}")