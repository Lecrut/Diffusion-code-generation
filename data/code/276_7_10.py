def repeat_elements(input_set, times):
    return input_set * times

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    repetitions = 4
    result = repeat_elements(sample_set, repetitions)
    print(result)