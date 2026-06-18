def combine_strings():
    s1 = "Hello"
    s2 = "World"
    return f"{s1}{s2}" if __name__ == '__main__' else lambda: None
if __name__ == '__main__':
    result = (lambda x, y: x + y)("Hello", "World")
    print(result)