def extract_first_letters(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    result_chars = [word[0].upper() for word in words]
    return "".join(result_chars)
if __name__ == '__main__':
    sample_input = "hello world python script execution"
    processed_output = extract_first_letters(sample_input)
    print(processed_output)