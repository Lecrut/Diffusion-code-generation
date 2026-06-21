import numpy as np

def calculate_range(data):
    if data.size == 0:
        return 0.0
    min_value = np.min(data)
    max_value = np.max(data)
    range_value = max_value - min_value
    return range_value

if __name__ == '__main__':
    sample_data1 = np.array([1.5, 3.2, 0.9, 5.8, 2.1])
    result1 = calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = np.array([10.0, 5.0, 20.0, 1.0])
    result2 = calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    sample_data3 = np.array([7.7, 7.7, 7.7])
    result3 = calculate_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")
    sample_data4 = np.array([])
    result4 = calculate_range(sample_data4)
    print(f"Data: {sample_data4}, Range: {result4}")