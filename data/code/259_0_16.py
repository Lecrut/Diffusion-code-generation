def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = largest = data[0]
    for x in data[1:]:
        if x < smallest:
            smallest = x
        elif x > largest:
            largest = x
    return smallest, largest

if __name__ == '__main__':
    sample_list = [56, 23, 89, 72, 1, 45]
    try:
        min_val, max_val = find_min_max(sample_list)
        print(f"Smallest value: {min_val}")
        print(f"Largest value: {max_val}")
    except ValueError as e:
        print(e)