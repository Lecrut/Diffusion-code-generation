import numpy as np

def calculate_average(data):
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [3.5, 2.8, 4.1, 3.9, 3.2]
    average = calculate_average(sample_data)
    print(average)