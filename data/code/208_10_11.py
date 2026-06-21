import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    list1 = [5, 10, 15, 20, 25]
    list2 = [3.5, 7.5, 11.5, 15.5, 19.5]
    empty_list = []
    list3 = [-5, 0, 5, 10]

    mean1 = calculate_mean(list1)
    mean2 = calculate_mean(list2)
    mean_empty = calculate_mean(empty_list)
    mean3 = calculate_mean(list3)

    print(f"Mean of {list1}: {mean1}")
    print(f"Mean of {list2}: {mean2}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {list3}: {mean3}")