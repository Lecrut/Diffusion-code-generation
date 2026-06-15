def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum
if __name__ == '__main__':
    large_list = [3.14159, -0.5, 100.2, -99.999, 5.00001, 0.0]
    minimum_value = find_minimum(large_list)
    print(minimum_value)