def validate_strings(str1: str, str2: str) -> bool:
    return isinstance(str1, str) and isinstance(str2, str)

def interleave_strings(str1: str, str2: str) -> str:
    if not validate_strings(str1, str2):
        raise ValueError("Both inputs must be strings")
    return f"{str1}{str2}"

if __name__ == '__main__':
    result = interleave_strings('hello', 'world')
    print(result)