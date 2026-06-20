def find_middle_element(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    try:
        result = find_middle_element(sample_list)
        print(result)
    except ValueError as e:
        print(e)