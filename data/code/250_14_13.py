import numpy as np

def calculate_average(data):
    return np.mean(data, dtype=np.float64)

if __name__ == '__main__':
    sample_data = [85.0, 92.0, 78.0]
    avg = calculate_average(sample_data)
    print(avg)