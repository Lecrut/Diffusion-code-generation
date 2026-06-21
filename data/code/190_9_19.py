import bisect

def contains_integer(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    target_number = 5
    result = contains_integer(sample_list, target_number)
    print(f"Number {target_number} is in the list: {result}")