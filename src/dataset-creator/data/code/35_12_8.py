import bisect
def find_target(sorted_list, target):
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return -1
if __name__ == '__main__':
    data = [3, 5, 7, 9, 12, 14, 16, 18, 20]
    test_values = [5, 12, 25, 12]
    for val in test_values:
        pos = find_target(data, val)
        if pos != -1:
            print(f"Found {val} at position {pos}")
        else:
            print(f"{val} not found")