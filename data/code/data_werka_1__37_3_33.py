def combine_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) > 1 and isinstance(args[0], str) and isinstance(args[1], str):
            combined_result = args[0] + " " + args[1]
            return combined_result
        return result
    return wrapper

@combine_results
def sample_function(a, b):
    return a, b

if __name__ == '__main__':
    print(sample_function("Hello", "World"))