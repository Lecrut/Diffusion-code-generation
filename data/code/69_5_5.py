import numpy as np

def miles_to_feet(miles_array):
    miles_array = np.asarray(miles_array, dtype=np.float64)
    return miles_array * 5280.0
if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 0.5, 10.0, 0.125])
    feet_result = miles_to_feet(sample_miles)
    print(feet_result)