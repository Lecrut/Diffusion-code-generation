import bisect

def is_integer_in_list(target, sorted_list):
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(is_integer_in_list(3, sample_list))
    print(is_integer_in_list(4, sample_list))