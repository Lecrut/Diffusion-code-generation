def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[:1].upper() + s[1:].lower()

if __name__ == '__main__':
    result = capitalize_first("hELLO wORLD")
    print(result)