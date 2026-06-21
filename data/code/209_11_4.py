import numpy as np

def calculate_average(data):
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [34, 56, 23, 89, 78]
    average = calculate_average(sample_data)
    print(average)