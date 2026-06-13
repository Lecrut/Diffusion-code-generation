def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    sample_list = [12, 45, 67, 89, 34, 91, 5]
    largest_number = find_largest(sample_list)
    print(largest_number)