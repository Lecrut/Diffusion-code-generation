def repeat_list_and_flatten(input_list, times):
    repeated_list = input_list * times
    return tuple(repeated_list)

if __name__ == '__main__':
    sample_list = [10, 20]
    repetitions = 7
    result = repeat_list_and_flatten(sample_list, repetitions)
    print(result)