def find_min_max(data):
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")