def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum
if __name__ == '__main__':
    large_list = [3.14159, -0.5, 100.0, -99.999, 2.71828, -1.0]
    try:
        min_value = find_minimum(large_list)
        print(min_value)
    except ValueError as e:
        print(f"Error: {e}")