def extend_string(pattern, repetitions):
    return pattern * repetitions

if __name__ == '__main__':
    pattern = 'AB'
    repetitions = 1000
    result = extend_string(pattern, repetitions)
    print(result)