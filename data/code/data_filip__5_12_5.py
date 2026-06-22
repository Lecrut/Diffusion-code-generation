def capitalize_first(text: str) -> str:
    return text[0].upper() + text[1:].lower() if text else ""

if __name__ == '__main__':
    print(capitalize_first("hello WORLD"))
    print(capitalize_first(""))