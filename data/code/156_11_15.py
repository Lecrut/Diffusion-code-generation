import numpy as np

def calculate_average(data):
    if not data:
        return 0
    return np.mean(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(f"Average of {sample_data}: {calculate_average(sample_data)}")