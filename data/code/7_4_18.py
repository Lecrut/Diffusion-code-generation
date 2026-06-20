import string

def find_first_special_char(text: str):
    special_chars = set(string.punctuation)
    for char in text:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Hello! World",
        "No special chars here 123",
        "@#$%",
        ""
    ]
    for sample in samples:
        print(f'"{sample}" -> "{find_first_special_char(sample)}"')