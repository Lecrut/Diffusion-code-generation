import bisect

def is_integer_in_sorted_list(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    if index != len(sorted_list) and sorted_list[index] == target:
        return True
    return False

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(f"Is 3 in the list? {is_integer_in_sorted_list(sample_list, 3)}")
    print(f"Is 4 in the list? {is_integer_in_sorted_list(sample_list, 4)}")