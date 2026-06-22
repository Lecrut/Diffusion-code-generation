def capitalize_and_lower(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    result = capitalize_and_lower("hELLO wORLD")
    print(result)