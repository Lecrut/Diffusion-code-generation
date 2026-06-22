import numpy as np

def convert_miles_to_feet(miles_array):
    miles_array = np.asarray(miles_array)
    return miles_array * 5280

if __name__ == '__main__':
    sample_miles = np.array([0.5, 1.0, 2.5, 10.0, 100.0])
    feet_result = convert_miles_to_feet(sample_miles)
    print(feet_result)