def join_strings_with_fstring(str1: str, str2: str) -> str:
    """Joins two strings using an f-string."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    result = join_strings_with_fstring("Hello", "World")
    print(result)