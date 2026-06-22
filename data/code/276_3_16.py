def repeat_string(s, p):
    if not isinstance(s, str) or not isinstance(p, int) or p < 0:
        raise ValueError("Invalid input")
    return s * p

if __name__ == '__main__':
    sample_string = "abc"
    times = 3
    result = repeat_string(sample_string, times)
    print(result)