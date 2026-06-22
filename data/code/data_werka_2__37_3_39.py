def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) != 2 or not all(isinstance(arg, str) for arg in args):
            raise ValueError("Function must be called with exactly two string arguments.")
        return result + " Combined"
    return wrapper

@combine_strings
def concatenate_strings(a, b):
    return a + b

if __name__ == '__main__':
    print(concatenate_strings("Hello", "World"))