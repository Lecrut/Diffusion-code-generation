def find_middle_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    n = len(data)
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    try:
        print(find_middle_element(sample_data))
    except ValueError as e:
        print(e)