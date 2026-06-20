def has_special_chars(text: str) -> bool:
    special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'}
    return bool(set(text) & special_chars)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = has_special_chars(sample_string)
    print(result)