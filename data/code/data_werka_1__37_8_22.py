def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings.")
    return str1 + str2

if __name__ == '__main__':
    try:
        string_a = "Hello"
        string_b = "World"
        result1 = combine_strings(string_a, string_b)
        print(result1)

        string_c = "Python"
        string_d = "Programming"
        result2 = combine_strings(string_d, string_c)
        print(result2)

    except ValueError as e:
        print(e)