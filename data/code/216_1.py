def find_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    middle_value = find_middle(sample_list)
    print(middle_value)