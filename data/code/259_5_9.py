def find_min_max(iterable):
    current_min = float('inf')
    current_max = float('-inf')
    for item in iterable:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    return current_min, current_max

if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    print("Data 1:")
    min_val, max_val = find_min_max(data1)
    print(f"Min: {min_val}, Max: {max_val}")

    data2 = [10, 45, -1, 7, 36, 89]
    print("\nData 2:")
    min_val, max_val = find_min_max(data2)
    print(f"Min: {min_val}, Max: {max_val}")