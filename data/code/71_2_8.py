def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    if n % 2 == 1:
        return data[middle_index]
    else:
        return (data[middle_index - 1] + data[middle_index]) / 2

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    middle_value = find_middle_value(sample_list)
    print(middle_value)