def find_minimum(data: list) -> int:
    if not data:
        raise ValueError("List cannot be empty")
    current_min = data[0]
    for element in data[1:]:
        if element < current_min:
            current_min = element
    return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(e)