import numpy as np

def find_data_range(data):
    if not data:
        return 0.0
    data_array = np.array(data)
    minimum = np.min(data_array)
    maximum = np.max(data_array)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [1.5, 3.2, 0.9, 5.8, 2.1]
    result1 = find_data_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = [10.0, 5.0, 20.0, 1.0]
    result2 = find_data_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")