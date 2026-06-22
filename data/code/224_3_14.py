import numpy as np

def calculate_average(values):
    if isinstance(values, np.ndarray):
        return np.mean(values)
    else:
        return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [2.5, 3.5, 4.5, 5.5]
    average_value = calculate_average(sample_values)
    print(average_value)