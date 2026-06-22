def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) != 2 or not all(isinstance(arg, str) for arg in args):
            raise ValueError("Function must accept exactly two string arguments.")
        combined_result = args[0] + " " + args[1]
        return combined_result
    return wrapper

@combine_strings
def greet(first_name, last_name):
    return first_name + " " + last_name

if __name__ == '__main__':
    try:
        greeting = greet("Alice", "Smith")
        print(greeting)
    except ValueError as e:
        print(e)