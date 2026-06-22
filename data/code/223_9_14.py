import numpy as np

def find_maximum_value(data):
    return np.max(data)

if __name__ == '__main__':
    input_data = [25, 40, 15, 35, 5]
    max_value = find_maximum_value(input_data)
    print(max_value)