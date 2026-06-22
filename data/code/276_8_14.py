def repeat_chars(input_string, times):
    return ''.join([char * times for char in input_string])
if __name__ == '__main__':
    test_string = 'abc'
    repetitions = 3
    result = repeat_chars(test_string, repetitions)
    print(result)