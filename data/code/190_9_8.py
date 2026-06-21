import bisect

def is_integer_in_list(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_value = 7
    print(is_integer_in_list(sample_list, target_value))