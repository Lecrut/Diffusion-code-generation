import numpy as np

def calculate_small_set_average(list_of_lists):
    return [np.mean(inner_list) if inner_list else 0 for inner_list in list_of_lists]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5]
    ]
    result = calculate_small_set_average(sample_data)
    print(result)