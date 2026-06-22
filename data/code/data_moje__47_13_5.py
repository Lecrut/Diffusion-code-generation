import numpy as np

def calculate_mean(data: np.ndarray) -> float:
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    result = calculate_mean(sample_data)
    print(result)