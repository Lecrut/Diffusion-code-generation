import numpy as np

def miles_to_feet_vectorized(miles_array):
    return np.asarray(miles_array, dtype=float) * 5280.0

if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 0.5, 10.0, 3.14159])
    result = miles_to_feet_vectorized(sample_miles)
    print(result)