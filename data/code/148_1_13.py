def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for number in data:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [15, 22, 8, 34, 67, 90, 21, 55, 88, 45]
    result = find_largest(sample_list)
    print(result)