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
    sample_list = [1, 5, 2, 8, 3]
    middle = find_middle_value(sample_list)
    print(middle)

    sample_list_even = [10, 20, 30, 40]
    middle_even = find_middle_value(sample_list_even)
    print(middle_even)