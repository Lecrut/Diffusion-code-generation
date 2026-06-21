import numpy as np

def calculate_mean_numpy(array):
    return np.mean(array)

if __name__ == '__main__':
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([10.5, 20.5, 30.5])
    empty_array = np.array([])
    array3 = np.array([-1, 5, 10, -2])

    mean1 = calculate_mean_numpy(array1)
    mean2 = calculate_mean_numpy(array2)
    mean_empty = calculate_mean_numpy(empty_array)
    mean3 = calculate_mean_numpy(array3)

    print(f"Mean of {array1}: {mean1}")
    print(f"Mean of {array2}: {mean2}")
    print(f"Mean of {empty_array}: {mean_empty}")
    print(f"Mean of {array3}: {mean3}")