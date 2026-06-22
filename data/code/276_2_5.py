def repeat_tuple_elements(input_tuple, k):
    return tuple(element * k for element in input_tuple)

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    k = 3
    result = repeat_tuple_elements(sample_tuple, k)
    print(result)