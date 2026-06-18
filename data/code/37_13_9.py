def join_strings(str1: str, str2: str) -> str:
    """Join two strings using an f-string."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    name = "Alice"
    greeting = "Hello!"
    result = join_strings(name, greeting)
    print(result)