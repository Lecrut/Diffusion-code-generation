def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_middle_element(sample_list)
    print(result)