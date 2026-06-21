import numpy as np

def calculate_mean(numbers):
    return np.mean(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-1, 5, 10, -2]
    mean1 = calculate_mean(np.array(list1))
    mean2 = calculate_mean(np.array(list2))
    mean_empty = calculate_mean(np.array(empty_list))
    mean3 = calculate_mean(np.array(list3))
    print(f"Mean of {list1}: {mean1}")
    print(f"Mean of {list2}: {mean2}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {list3}: {mean3}")