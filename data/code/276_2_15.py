def repeat_tuple_elements(input_tuple, k):
    return input_tuple * k

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    times = 3
    result = repeat_tuple_elements(sample_tuple, times)
    print(result)