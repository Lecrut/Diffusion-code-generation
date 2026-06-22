def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            return args[0] + args[1]
        return result
    return wrapper

@combine_strings
def sample_function(a, b):
    return a, b

if __name__ == '__main__':
    combined_result = sample_function("Hello, ", "World!")
    print(combined_result)