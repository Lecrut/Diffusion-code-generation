def strip_whitespace(text):
    if text is None:
        return ""
    if isinstance(text, str):
        return text.strip()
    return str(text).strip()

if __name__ == '__main__':
    result1 = strip_whitespace("  hello  ")
    print(result1)
    result2 = strip_whitespace(123)
    print(result2)
    result3 = strip_whitespace(None)
    print(result3)
    result4 = strip_whitespace([1, 2, 3])
    print(result4)