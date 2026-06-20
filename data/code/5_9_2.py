def capitalize_first(text):
    if not text:
        return text
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    result = capitalize_first("hELLO wORLD")
    print(result)