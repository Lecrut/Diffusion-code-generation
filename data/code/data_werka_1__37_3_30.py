def combine_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) == 2:
            return result[0] + result[1]
        return result
    return wrapper

@combine_results
def process_strings(str1, str2):
    return (str1, str2)

if __name__ == '__main__':
    combined_string = process_strings("Hello, ", "World!")
    print(combined_string)