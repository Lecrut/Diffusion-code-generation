def combine_strings(func):
    def wrapper(str1, str2):
        return str1 + str2
    return wrapper
@combine_strings
def string_combiner(a, b):
    return a, b
if __name__ == '__main__':
    result = string_combiner("Hello, ", "World!")
    print(result)