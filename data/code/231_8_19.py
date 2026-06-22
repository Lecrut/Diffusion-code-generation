def repeat_and_flatten(input_list, repeat_count):
    return tuple(item for sublist in [input_list] * repeat_count for item in sublist)

if __name__ == '__main__':
    sample_list = [10, 20]
    repetitions = 7
    result = repeat_and_flatten(sample_list, repetitions)
    print(result)