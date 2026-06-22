def find_min_max(data):
    if not data:
        return None, None
    smallest = min(data)
    largest = max(data)
    return smallest, largest

if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 91, 50, 1]
    print("Original List:", large_list)
    min_val, max_val = find_min_max(large_list)
    print("Calculated Smallest Element:", min_val)
    print("Calculated Largest Element:", max_val)