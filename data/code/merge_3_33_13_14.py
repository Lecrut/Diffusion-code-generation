def remove_spaces(s: str) -> str:
    """Returns a copy of string s with all spaces removed."""
    return "".join(c for c in s if not c.isspace())

if __name__ == '__main__':
    samples = ["Hello World", "Python 3.12 is great!", "NoSpacesHere"]
    for sample in samples:
        print(remove_spaces(sample))