import numpy as np

def miles_to_feet(miles_array):
    conversion_factor = 5280.0
    return miles_array * conversion_factor

if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 10.0, 0.5])
    result_feet = miles_to_feet(sample_miles)
    print(result_feet)