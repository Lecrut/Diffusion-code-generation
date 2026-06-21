import numpy as np

def calculate_average(data):
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [4.5, 9.2, 3.8, 6.1]
    average = calculate_average(sample_data)
    print(f"Average of {sample_data}: {average}")