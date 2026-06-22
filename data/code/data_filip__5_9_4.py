def capitalize_first_char(text):
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample_strings = ["hELLO wORLD", "python", "PyThOn", "a", "", "TEST"]
    for s in sample_strings:
        result = capitalize_first_char(s)
        print(f"Input: '{s}' -> Output: '{result}'")