def get_string_length(s: str) -> int:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return len(s)

if __name__ == '__main__':
    sample_texts = ["Hello, World!", "", "Python programming", "  \t\n"]
    for text in sample_texts:
        print(f'Length of "{text}": {get_string_length(text)}')