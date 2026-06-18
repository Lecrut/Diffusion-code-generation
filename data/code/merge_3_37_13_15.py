def join_strings(a: str, b: str) -> str:
    """Joins two strings using an f-string."""
    return f"{a} {b}"

if __name__ == '__main__':
    sample_1 = "Hello"
    sample_2 = "World"
    result = join_strings(sample_1, sample_2)
    print(result)