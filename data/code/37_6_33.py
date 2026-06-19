def interleave_strings(str1: str, str2: str) -> str:
    if not isinstance(str1, str):
        raise ValueError("The first argument must be a string.")
    if not isinstance(str2, str):
        raise ValueError("The second argument must be a string.")
    
    return f"{str1}{str2}"

if __name__ == '__main__':
    try:
        result = interleave_strings('hello', 'world')
        print(result)
    except ValueError as e:
        print(e)