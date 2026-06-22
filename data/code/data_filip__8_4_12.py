def split_and_strip(string: str) -> list:
    return [token.strip() for token in string.split(',') if token.strip()]

if __name__ == '__main__':
    result = split_and_strip("  hello , world ,  python  ")
    print(result)