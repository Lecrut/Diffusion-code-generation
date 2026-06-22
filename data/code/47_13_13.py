import numpy as np

def calculate_mean(data: list[float]) -> float:
    arr = np.array(data)
    return float(np.mean(arr))

if __name__ == '__main__':
    data_points = [10, 20, 30, 40, 50]
    result = calculate_mean(data_points)
    print(result)