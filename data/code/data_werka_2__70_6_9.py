def process_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return None, None
    tokens = text.split()
    if not tokens:
        return None, None
    return tokens[0], tokens[-1]

if __name__ == '__main__':
    data = "Performance optimization is critical for large inputs"
    result = process_text(data)
    print(result)