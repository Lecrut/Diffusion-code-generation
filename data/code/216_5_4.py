def middle_value_generator(data):
    n = len(data)
    if n == 0:
        return
    for i in range(n // 2):
        yield data[i]
if __name__ == '__main__':
    large_list = list(range(1000000))
    middle_values = middle_value_generator(large_list)
    result_list = list(middle_values)
    print(result_list)