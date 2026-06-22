def normalize_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    sample_data = "   Hello World   "
    result = normalize_text(sample_data)
    print(result)
    another_sample = "\t\n  Python Code  \t\n"
    print(normalize_text(another_sample))
    empty_sample = "   "
    print(repr(normalize_text(empty_sample)))