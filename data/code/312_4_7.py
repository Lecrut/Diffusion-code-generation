def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    large_list = [3.14159, 2.71828, 1.61803, 0.57721, 9.81, -5.0]
    result = find_largest(large_list)
    print(result)