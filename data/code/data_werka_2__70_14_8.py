def get_boundary_elements(data):
    if len(data) == 0:
        raise ValueError("List must not be empty")
    start_index = 0
    end_index = len(data) - 1
    first_item = data[start_index]
    last_item = data[end_index]
    return first_item, last_item

if __name__ == '__main__':
    test_values = [10, 20, 30, 40, 50]
    boundary_result = get_boundary_elements(test_values)
    print(boundary_result)