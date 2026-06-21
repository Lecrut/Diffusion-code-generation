import bisect

def is_integer_in_sorted_list(sorted_list, target):
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("All elements in the list must be integers.")
    if not isinstance(target, int):
        raise ValueError("Target must be an integer.")
    
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(f"Is 4 in the list? {is_integer_in_sorted_list(sample_list, 4)}")
    print(f"Is 7 in the list? {is_integer_in_sorted_list(sample_list, 7)}")