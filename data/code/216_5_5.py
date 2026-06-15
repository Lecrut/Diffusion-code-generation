def middle_value_generator(data):
    n = len(data)
    if n == 0:
        return
    for i in range(n // 2):
        yield data[i]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator = middle_value_generator(sample_list)
    result = list(generator)
    print(result)
    sample_list_odd = [1, 2, 3, 4, 5]
    generator_odd = middle_value_generator(sample_list_odd)
    result_odd = list(generator_odd)
    print(result_odd)
    sample_list_large = list(range(1000000))
    generator_large = middle_value_generator(sample_list_large)
    result_large = list(generator_large)
    print(result_large)