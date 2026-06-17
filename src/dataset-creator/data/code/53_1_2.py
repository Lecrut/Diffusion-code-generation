def count_elements(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    data_tuple = (6, 7, 8)
    data_set = {9, 10}
    print(count_elements(data_list))
    print(count_elements(data_tuple))
    print(count_elements(data_set))