def capitalize_first_alnum(text):
    if not text:
        return text
    for i, char in enumerate(text):
        if char.isalnum():
            return text[:i] + char.upper() + text[i + 1:]
    return text

if __name__ == '__main__':
    examples = ["123abc", "abc", "  hello", "!@#World", ""]
    for example in examples:
        result = capitalize_first_alnum(example)
        print(result)