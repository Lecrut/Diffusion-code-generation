import re

def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    samples = ["Hello World", "  Leading and Trailing Spaces  ", "NoSpacesHere"]
    for item in samples:
        print(f"Original: {item!r}")
        print(f"No spaces: {remove_spaces(item)}")