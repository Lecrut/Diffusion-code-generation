import numpy as np

def calculate_average(data):
    return np.mean(data).astype(float)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(sample_data)
    print(average)