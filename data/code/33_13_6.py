def remove_spaces(s: str) -> str:
    """Return a string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == "__main__":
    print(remove_spaces("Hello World"))  # Output: HelloWorld