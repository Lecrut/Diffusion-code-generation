def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings")
    return str1 + str2

if __name__ == '__main__':
    try:
        a = "hello"
        b = "world"
        result = combine_strings(a, b)
        print(result)
    except ValueError as e:
        print(e)