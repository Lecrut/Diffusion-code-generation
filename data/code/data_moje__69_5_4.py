import numpy as np

def miles_to_feet(miles_array):
    return miles_array * 5280

if __name__ == '__main__':
    mile_distances = np.array([1.0, 2.5, 10.0, 100.0])
    feet_distances = miles_to_feet(mile_distances)
    print(feet_distances)