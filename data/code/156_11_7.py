import numpy as np

def calculate_average(data):
    if not data:
        return 0
    return np.mean(data)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45]
    average_result = calculate_average(sample_data)
    print(f"Average of {sample_data}: {average_result}")