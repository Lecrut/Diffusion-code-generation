import numpy as np

def calculate_average(data):
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [34, 23, 56, 78, 90]
    average = calculate_average(sample_data)
    print(average)