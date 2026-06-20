def capitalize_first(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    sample = "hELLO wORLD"
    result = capitalize_first(sample)
    print(result)