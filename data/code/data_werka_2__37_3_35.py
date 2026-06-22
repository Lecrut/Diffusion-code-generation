def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) != 2 or not all(isinstance(item, str) for item in result):
            raise ValueError("Function must return a tuple of two strings")
        return result[0] + result[1]
    return wrapper

@combine_strings
def get_strings():
    return "Hello", "World"

if __name__ == '__main__':
    combined_result = get_strings()
    print(combined_result)