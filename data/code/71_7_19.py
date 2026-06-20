def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [4, 7, 1, 3, 6, 9]
    result = find_middle_element(sample_list)
    print(result)