def combine_strings():
    s1 = "Hello"
    s2 = "World"
    return lambda: f"{s1} {s2}" if __name__ == '__main__' else None
if __name__ == '__main__':
    result = combine_strings()
    print(result())