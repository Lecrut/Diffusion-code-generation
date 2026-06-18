def join_strings(a: str, b: str) -> str:
    """Joins two strings using an f-string."""
    return f"{a}{b}"

if __name__ == '__main__':
    result = join_strings("Hello", "World")
    print(result)