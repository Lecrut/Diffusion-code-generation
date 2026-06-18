def remove_spaces(s: str) -> str:
    """Returns a new string with all spaces removed."""
    return "".join(c for c in s if not c.isspace())

if __name__ == '__main__':
    samples = ["Hello World", "  Multiple   Spaces  ", "NoSpacesAtAll"]
    print(remove_spaces(" ".join(samples)))