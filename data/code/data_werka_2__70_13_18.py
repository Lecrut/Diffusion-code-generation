def get_first_last(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        raise ValueError("Input must not be empty")
    return (s[0], s[-1])

if __name__ == '__main__':
    sample = "speed"
    result = get_first_last(sample)
    print(result)