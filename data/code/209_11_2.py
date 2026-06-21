import numpy as np

def calculate_average(data):
    return np.mean(data).astype(float)

if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 11]
    average = calculate_average(sample_data)
    print(average)