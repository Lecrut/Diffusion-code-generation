def process_string(s: str) -> tuple[str, str, str]:
    """Returns a tuple with (original string, lowercase version, reversed case version)."""
    return s, s.lower(), ''.join(c.swapcase() if i % 2 == 0 else c for i in range(len(s)))

if __name__ == '__main__':
    sample = "Hello World"
    result = process_string(sample)
    print(f"{result[0]!r}, {result[1]}, {result[2]}")