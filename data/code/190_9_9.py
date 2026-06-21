import bisect

def is_integer_in_list(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    target_value = 5
    print(is_integer_in_list(sample_list, target_value))