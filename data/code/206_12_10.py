def find_minimum(data):
    if not data:
        raise ValueError("List cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, -9, 23, 89]
    min_value = find_minimum(sample_list)
    print(f"Minimum of {sample_list} is: {min_value}")