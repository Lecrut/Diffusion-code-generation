def repeat_set_elements(input_set, repetitions):
    return input_set * repetitions

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    sample_repetitions = 3
    repeated_result = repeat_set_elements(sample_set, sample_repetitions)
    print(repeated_result)