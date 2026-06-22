import numpy as np

def validate_input(list_of_lists):
    if not all(isinstance(sublist, list) for sublist in list_of_lists):
        raise ValueError("All elements must be lists.")
    if not all(all(isinstance(item, int) for item in sublist) for sublist in list_of_lists):
        raise ValueError("All elements within sublists must be integers.")

def calculate_small_set_average(list_of_lists):
    validate_input(list_of_lists)
    
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
        [10, 20],
        [5, 5, 5, 5]
    ]
    result = calculate_small_set_average(sample_data)
    print(result)