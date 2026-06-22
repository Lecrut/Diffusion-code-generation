def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")

def interleave_strings(str1: str, str2: str) -> str:
    validate_strings(str1, str2)
    return f"{str1}{str2}"

if __name__ == '__main__':
    result = interleave_strings('hello', 'world')
    print(result)