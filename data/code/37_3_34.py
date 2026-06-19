def combine_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) == 2 and all(isinstance(item, str) for item in result):
            return result[0] + result[1]
        return result
    return wrapper

@combine_strings
def get_strings():
    return "Hello", "World"

if __name__ == '__main__':
    print(get_strings())