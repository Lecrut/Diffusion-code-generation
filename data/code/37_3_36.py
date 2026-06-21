def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) != 2 or not all(isinstance(arg, str) for arg in args):
            raise ValueError("Function must be called with exactly two string arguments.")
        return result + " " + args[1]
    return wrapper

@combine_strings
def concatenate(a, b):
    return a

if __name__ == '__main__':
    print(concatenate("Hello", "World"))