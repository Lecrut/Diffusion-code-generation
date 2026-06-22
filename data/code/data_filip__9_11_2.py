def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    result = trim_string("  hello world  ")
    print(result)