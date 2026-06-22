import numpy as np

def miles_to_feet(miles_array):
    feet_per_mile = 5280
    return np.asarray(miles_array) * feet_per_mile

if __name__ == '__main__':
    sample_miles = np.array([0.5, 1.0, 2.5, 10.0, 100.0])
    result_feet = miles_to_feet(sample_miles)
    print(result_feet)