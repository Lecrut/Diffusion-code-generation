def combine_decorator(func):
    def wrapper(str1, str2):
        result = func(str1, str2)
        return result + " Combined"
    return wrapper

@combine_decorator
def concatenate_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    result = concatenate_strings(string_a, string_b)
    print(result)