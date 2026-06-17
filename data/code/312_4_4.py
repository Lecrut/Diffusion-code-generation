def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    large_list = [3.1415926535, 2.7182818284, 1.6180339887, 99.9999999999, -5.0, 1000.0]
    result = find_largest(large_list)
    print(result)