def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for number in data[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_largest(sample_list)
    print(result)