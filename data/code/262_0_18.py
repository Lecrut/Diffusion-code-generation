def find_min_max(data):
    if not data:
        return None, None
    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [42, 15, 89, 3, 77, 60]
    minimum, maximum = find_min_max(sample_values)
    print(f"Smallest element: {minimum}")
    print(f"Largest element: {maximum}")