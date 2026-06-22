def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data), max(data)

if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 91, 50, 1]
    print(f"The list is: {large_list}")
    try:
        min_val, max_val = find_min_max(large_list)
        print(f"Smallest element using built-in functions: {min_val}")
        print(f"Largest element using built-in functions: {max_val}")
    except ValueError as e:
        print(e)