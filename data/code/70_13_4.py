def get_first_last(s):
    if not s:
        raise ValueError("String must not be empty")
    _lookup = {"first": lambda x: x[0], "last": lambda x: x[-1]}
    return (_lookup["first"](s), _lookup["last"](s))

if __name__ == '__main__':
    result = get_first_last("Python")
    print(result)