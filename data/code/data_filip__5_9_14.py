def capitalize_first_lower_rest(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    sample_1 = "hELLO wORLD"
    sample_2 = "PYtHoN"
    sample_3 = "a"
    sample_4 = ""
    sample_5 = "tHe QuIcK BrOwN fOx"
    
    print(capitalize_first_lower_rest(sample_1))
    print(capitalize_first_lower_rest(sample_2))
    print(capitalize_first_lower_rest(sample_3))
    print(capitalize_first_lower_rest(sample_4))
    print(capitalize_first_lower_rest(sample_5))