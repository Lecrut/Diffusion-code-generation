import numpy as np

def miles_to_feet(miles_array):
    conversion_factor = 5280.0
    return np.asarray(miles_array, dtype=np.float64) * conversion_factor

if __name__ == '__main__':
    sample_miles = np.array([1, 5, 10, 26.2, 0.5])
    result_feet = miles_to_feet(sample_miles)
    print(result_feet)