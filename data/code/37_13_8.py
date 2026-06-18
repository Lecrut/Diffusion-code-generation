def join_strings(str1: str, str2: str) -> str:
    """Joins two strings using an f-string."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    result = join_strings("Hello", "World")
    print(result)