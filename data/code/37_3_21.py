def combine_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) != 2 or not all(isinstance(item, str) for item in result):
            raise ValueError("Function must return a tuple of two strings.")
        combined_result = result[0] + result[1]
        return combined_result
    return wrapper

@combine_results
def get_strings():
    return "Hello", "World"

if __name__ == '__main__':
    print(get_strings())