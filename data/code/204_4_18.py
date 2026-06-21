import bisect

def get_central_value(sorted_list):
    n = len(sorted_list)
    if n == 0:
        raise ValueError("Cannot find the middle of an empty list")
    middle_index = n // 2
    return sorted_list[middle_index]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    central_value1 = get_central_value(sample_list1)
    print(f"Central value of {sample_list1}: {central_value1}")

    sample_list2 = [2, 4, 6, 8, 10, 12]
    central_value2 = get_central_value(sample_list2)
    print(f"Central value of {sample_list2}: {central_value2}")