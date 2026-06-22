import numpy as np

def miles_to_feet(miles_array):
    return miles_array * 5280
if __name__ == '__main__':
    distances = np.array([1.0, 2.5, 10.0, 0.5])
    result = miles_to_feet(distances)
    print(result)