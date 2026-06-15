def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum
if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 56, 91, 22, 78, 10]
    min_element = find_minimum(large_list)
    print(min_element)