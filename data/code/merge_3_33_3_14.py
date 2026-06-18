import re

def remove_spaces(s: str) -> str:
    return s.replace(' ', '') if isinstance(s, str) else ''

if __name__ == '__main__':
    samples = [
        "Hello World",
        "  Multiple   Spaces ",
        "",
        "NoSpacesHere"
    ]
    for sample in samples:
        print(remove_spaces(sample))