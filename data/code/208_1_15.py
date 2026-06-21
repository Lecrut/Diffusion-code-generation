import numpy as np

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return np.mean(np.array(numbers))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-1, 5, 10, -2]

    try:
        mean1 = calculate_mean(list1)
        print(f"Mean of {list1}: {mean1}")
    except ValueError as e:
        print(e)

    try:
        mean2 = calculate_mean(list2)
        print(f"Mean of {list2}: {mean2}")
    except ValueError as e:
        print(e)

    try:
        mean_empty = calculate_mean(empty_list)
    except ValueError as e:
        print(e)

    try:
        mean3 = calculate_mean(list3)
        print(f"Mean of {list3}: {mean3}")
    except ValueError as e:
        print(e)