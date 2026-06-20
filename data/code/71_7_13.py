def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    mid_index = n // 2
    return data[mid_index]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = find_middle_element(sample_list)
    print(result)