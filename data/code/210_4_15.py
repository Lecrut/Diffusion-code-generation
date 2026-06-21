def find_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_range(sample_values)
    print(f"Range of {sample_values}: {result}")