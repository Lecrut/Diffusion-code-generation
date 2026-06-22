def sanitize_string(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    raw_input = "   Python is elegant   "
    result = sanitize_string(raw_input)
    print(result)