def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")

def combine_strings(str1, str2):
    validate_strings(str1, str2)
    return f"{str1} {str2}"

if __name__ == '__main__':
    greeting = "Hello"
    farewell = "World"
    try:
        result = combine_strings(greeting, farewell)
        print(result)
    except ValueError as e:
        print(e)