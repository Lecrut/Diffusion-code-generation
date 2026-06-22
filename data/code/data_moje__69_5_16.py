import numpy as np

def miles_to_feet(miles):
    return np.asarray(miles) * 5280

if __name__ == '__main__':
    sample_miles = np.array([1.0, 2.5, 0.5, 10.0])
    print(miles_to_feet(sample_miles))