def middle_value_generator(data):
    n = len(data)
    if n == 0:
        return
    for i in range(n // 2):
        yield data[i]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(middle_value_generator(sample_list)))
    large_list = list(range(1000000))
    print(list(middle_value_generator(large_list)))
    empty_list = []
    print(list(middle_value_generator(empty_list)))