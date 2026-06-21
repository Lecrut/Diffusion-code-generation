def get_first_last(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        raise ValueError("Input must not be empty")
    _indices = {
        "first": 0,
        "last": -1
    }
    return (s[_indices["first"]], s[_indices["last"]])

if __name__ == '__main__':
    result = get_first_last("Python")
    print(result)