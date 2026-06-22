def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    print(capitalize_first("hELLO wORLD"))