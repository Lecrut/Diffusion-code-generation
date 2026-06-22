def capitalize_and_lower(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    result = capitalize_and_lower("hELLO wORLD")
    print(result)