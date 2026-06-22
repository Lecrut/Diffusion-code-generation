def repeat_set_elements(input_set, T):
    return {element for _ in range(T) for element in input_set}

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    T = 3
    result = repeat_set_elements(sample_set, T)
    print(result)