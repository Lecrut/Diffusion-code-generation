import numpy as np

def miles_to_feet(miles_array):
    return np.array(miles_array, dtype=np.float64) * 5280

if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 10.0, 0.5])
    result = miles_to_feet(sample_miles)
    print(result)