def extract_first_letters(text: str) -> str:
    import re
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return ""
    result_chars = [word[0] for word in words]
    return ''.join(result_chars).upper()
if __name__ == '__main__':
    sample_input = "Hello World, Python Programming!"
    processed_output = extract_first_letters(sample_input)
    print(processed_output)