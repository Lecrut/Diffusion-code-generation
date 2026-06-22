def repeat_tuple_elements(input_tuple, K):
    return input_tuple * K

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    K = 3
    result = repeat_tuple_elements(sample_tuple, K)
    print(result)