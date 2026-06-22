def extract_boundary_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return None
    words = text.split()
    if not words:
        return None
    return words[0], words[-1]

if __name__ == '__main__':
    sample_text = "Performance optimization is critical for large inputs"
    result = extract_boundary_words(sample_text)
    print(result)