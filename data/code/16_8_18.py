import numpy as np

def get_first_value():
    vector = np.array([10, 20, 30, 40, 50])
    return vector[0]

if __name__ == '__main__':
    result = get_first_value()
    print(result)