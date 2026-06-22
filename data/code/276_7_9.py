def repeat_elements(s, t):
    return {x for _ in range(t) for x in s}

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    times = 3
    result = repeat_elements(sample_set, times)
    print(result)