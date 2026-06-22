import numpy as np

def miles_to_feet(miles: np.ndarray) -> np.ndarray:
    return miles * 5280

if __name__ == '__main__':
    miles_array = np.array([1.0, 2.5, 10.0, 0.5])
    feet_array = miles_to_feet(miles_array)
    print(feet_array)