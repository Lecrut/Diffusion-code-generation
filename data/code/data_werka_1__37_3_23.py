def combine_strings_decorator(func):
    def wrapper(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        result = func(str1, str2)
        return result
    return wrapper

@combine_strings_decorator
def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    try:
        result = combine_strings(string_a, string_b)
        print(result)
    except ValueError as e:
        print(e)