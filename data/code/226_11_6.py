def repeat_pattern(pattern, repetitions):
    return pattern * repetitions

if __name__ == '__main__':
    pattern = 'AB'
    repetitions = 1000
    result = repeat_pattern(pattern, repetitions)
    print(result)