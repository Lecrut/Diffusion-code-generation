def join_strings_with_fstring(s1: str, s2: str) -> str:
    """Joins two strings using an f-string."""
    return f"{s1} {s2}"

if __name__ == '__main__':
    name = "Alice"
    greeting = "Hello!"
    result = join_strings_with_fstring(name, greeting)
    print(result)