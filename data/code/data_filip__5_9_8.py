def capitalize_first_lower_rest(text: str) -> str:
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample1 = "hELLO wORLD"
    sample2 = "tEsT cAsE"
    sample3 = "a"
    sample4 = "ALL CAPS"
    
    print(capitalize_first_lower_rest(sample1))
    print(capitalize_first_lower_rest(sample2))
    print(capitalize_first_lower_rest(sample3))
    print(capitalize_first_lower_rest(sample4))