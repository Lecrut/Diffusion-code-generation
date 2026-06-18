def join_strings_with_f_string(s1: str, s2: str) -> str:
    """Joins two strings using an f-string."""
    return f"{s1}{s2}"

if __name__ == '__main__':
    result = join_strings_with_f_string("Hello", "World")
    print(result)