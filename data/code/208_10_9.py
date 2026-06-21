import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-10, 20, 30]

    print(f"Mean of {list1}: {calculate_mean(list1)}")
    print(f"Mean of {list2}: {calculate_mean(list2)}")
    print(f"Mean of {empty_list}: {calculate_mean(empty_list)}")
    print(f"Mean of {list3}: {calculate_mean(list3)}")