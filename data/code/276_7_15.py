def repeat_elements(input_set, times):
    result = set()
    for _ in range(times):
        result.update(input_set)
    return result

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    repetitions = 4
    repeated_result = repeat_elements(sample_set, repetitions)
    print(repeated_result)