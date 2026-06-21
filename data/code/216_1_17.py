def find_middle(data):
    if not data or len(data) <= 0:
        raise ValueError("Input list must not be empty")
    
    n = len(data)
    middle_index = n // 2
    
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    try:
        middle_value = find_middle(sample_list)
        print(middle_value)
    except ValueError as e:
        print(e)

    sample_list = [1, 2, 3, 4, 5]
    try:
        middle_value = find_middle(sample_list)
        print(middle_value)
    except ValueError as e:
        print(e)

    sample_list = [7]
    try:
        middle_value = find_middle(sample_list)
        print(middle_value)
    except ValueError as e:
        print(e)

    sample_list = [100, 200]
    try:
        middle_value = find_middle(sample_list)
        print(middle_value)
    except ValueError as e:
        print(e)