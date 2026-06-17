def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_minimum = data[0]
    for element in data[1:]:
        if element < current_minimum:
            current_minimum = element
    return current_minimum
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)