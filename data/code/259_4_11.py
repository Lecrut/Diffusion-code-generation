def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = min(data)
    largest = max(data)
    return smallest, largest

if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 91, 50, 1]
    try:
        min_val, max_val = find_min_max(large_list)
        print(f"The list is: {large_list}")
        print(f"Smallest element: {min_val}")
        print(f"Largest element: {max_val}")
    except ValueError as e:
        print(e)