import numpy as np

def miles_to_feet(miles):
    return np.asarray(miles) * 5280.0
if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 10.0, 0.5])
    result = miles_to_feet(sample_miles)
    print(result)