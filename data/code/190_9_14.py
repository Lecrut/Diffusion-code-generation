import bisect

def is_integer_in_list(sorted_numbers, target):
    index = bisect.bisect_left(sorted_numbers, target)
    return index != len(sorted_numbers) and sorted_numbers[index] == target

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    target1 = 35
    result1 = is_integer_in_list(sample_list1, target1)
    print(f"Target {target1} in list: {result1}")

    sample_list2 = [-5, -3, -1, 0, 2]
    target2 = -4
    result2 = is_integer_in_list(sample_list2, target2)
    print(f"Target {target2} in list: {result2}")