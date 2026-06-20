def capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:].lower() if s else s

if __name__ == '__main__':
    result = capitalize_first("hELLO wORLD")
    print(result)