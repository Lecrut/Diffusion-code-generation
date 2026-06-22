def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) >= 2:
            combined_result = args[0] + " " + args[1]
            return combined_result
        return result
    return wrapper

@combine_strings
def sample_function(a, b):
    return a + b

if __name__ == '__main__':
    result = sample_function("Hello", "World")
    print(result)