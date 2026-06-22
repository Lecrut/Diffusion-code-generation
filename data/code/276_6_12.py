def repeat_integers(input_list, S):
    return [x for x in input_list for _ in range(S)]

if __name__ == '__main__':
    sample_input = [1, 2, 3]
    S = 3
    result = repeat_integers(sample_input, S)
    print(result)