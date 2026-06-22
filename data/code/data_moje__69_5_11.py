import numpy as np

def convert_miles_to_feet(miles_array):
    feet_per_mile = 5280
    return miles_array * feet_per_mile

if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 10.0, 0.5])
    result = convert_miles_to_feet(sample_miles)
    print(result)