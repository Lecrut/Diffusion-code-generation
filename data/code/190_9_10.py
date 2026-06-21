import bisect

def contains_integer(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    search_value = 30
    result = contains_integer(sample_list, search_value)
    print(f"Does the list contain {search_value}? {result}")