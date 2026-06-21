def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError('Data list cannot be empty')
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = [4, 10, 7, 15, 9]
    try:
        print(find_middle(sample_list1))
        print(find_middle(sample_list2))
    except ValueError as e:
        print(e)