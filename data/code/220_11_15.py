import numpy as np

def calculate_small_set_average(list_of_lists):
    non_empty_lists = [np.array(inner_list) for inner_list in list_of_lists if inner_list]
    averages = np.mean(non_empty_lists, axis=1)
    return averages.tolist()

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5],
        []
    ]
    result = calculate_small_set_average(sample_data)
    print(result)