def get_first_last(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        raise ValueError("Input must not be empty")
    return (s[0], s[-1])

if __name__ == '__main__':
    result = get_first_last("Python")
    print(result)