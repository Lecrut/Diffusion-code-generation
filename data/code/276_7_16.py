def repeat_elements(s, t):
    return {element * t for element in s}

if __name__ == '__main__':
    sample_set = {'a', 'b', 'c'}
    times = 3
    result = repeat_elements(sample_set, times)
    print(result)