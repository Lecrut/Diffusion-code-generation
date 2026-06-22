import numpy as np

def calculate_small_set_average(list_of_lists):
    arrays = [np.array(inner_list) for inner_list in list_of_lists if inner_list]
    averages = np.mean(arrays, axis=1)
    return averages.tolist()

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5],
        [],
        [100]
    ]
    result = calculate_small_set_average(sample_data)
    print(result)