def capitalize_string(text: str) -> str:
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample_text = "hello WORLD"
    result = capitalize_string(sample_text)
    print(result)