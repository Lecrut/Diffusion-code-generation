def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [9, 5, 2, 8, 3]
    middle = find_middle_value(sample_list)
    print(middle)