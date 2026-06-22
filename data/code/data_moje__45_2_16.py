def find_minimum(data):
    if not data:
        raise ValueError("The list is empty")
    current_min = data[0]
    for item in data[1:]:
        if item < current_min:
            current_min = item
    return current_min

if __name__ == '__main__':
    numbers = [3.14, 1.41, 2.72, 0.57, 1.73]
    result = find_minimum(numbers)
    print(result)