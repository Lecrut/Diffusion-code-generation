import numpy as np

def miles_to_feet(miles_array):
    return miles_array * 5280

if __name__ == '__main__':
    sample_distances = np.array([0.5, 1.0, 2.5, 10.0, 100.0])
    result = miles_to_feet(sample_distances)
    print(result)