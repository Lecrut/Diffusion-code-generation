def capitalize_first(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample_input = "hELLO wORLD"
    result = capitalize_first(sample_input)
    print(result)