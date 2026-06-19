def join_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return f"{str1} {str2}"

if __name__ == '__main__':
    try:
        result = join_strings("Hello", "World")
        print(result)
    except ValueError as e:
        print(e)