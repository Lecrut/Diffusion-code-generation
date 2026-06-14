def find_min_max(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    current_min = data[0]
    current_max = data[0]
    for element in data[1:]:
        if element < current_min:
            current_min = element
        elif element > current_max:
            current_max = element
    return current_min, current_max
if __name__ == '__main__':
    sample1 = [10, -5, 20, 3, 15]
    minimum1, maximum1 = find_min_max(sample1)
    print(f"Sample 1: {sample1}")
    print(f"Minimum: {minimum1}, Maximum: {maximum1}")
    sample2 = [-10, -2, -50, -1]
    minimum2, maximum2 = find_min_max(sample2)
    print(f"Sample 2: {sample2}")
    print(f"Minimum: {minimum2}, Maximum: {maximum2}")
    sample3 = [7, 7, 7, 7]
    minimum3, maximum3 = find_min_max(sample3)
    print(f"Sample 3: {sample3}")
    print(f"Minimum: {minimum3}, Maximum: {maximum3}")
    sample4 = [42]
    minimum4, maximum4 = find_min_max(sample4)
    print(f"Sample 4: {sample4}")
    print(f"Minimum: {minimum4}, Maximum: {maximum4}")
    try:
        sample5 = []
        find_min_max(sample5)
    except ValueError as e:
        print(f"Sample 5: {sample5}")
        print(f"Error caught: {e}")