def remove_spaces(s: str) -> str:
    """Returns a string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == '__main__':
    samples = ["Hello World", "Python is great   ", "  Spaces Everywhere  "]
    for sample in samples:
        print(remove_spaces(sample))