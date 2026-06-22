def repeat_elements(input_set, T):
    return input_set * T

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    T = 3
    result = repeat_elements(sample_set, T)
    print(result)