import numpy as np

def calculate_small_set_average(list_of_lists):
    averages = []
    for inner_list in list_of_lists:
        if inner_list:
            average = np.mean(inner_list)
            averages.append(average)
        else:
            averages.append(0)
    return averages

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20, 30],
        [5, 5, 5, 5]
    ]
    result = calculate_small_set_average(sample_data)
    print(result)