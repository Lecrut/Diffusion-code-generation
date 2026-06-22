def extract_first_word(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    parts = text.split()
    if parts:
        return parts[0].strip()
    return ""

if __name__ == '__main__':
    sample1 = "  Hello world! "
    result1 = extract_first_word(sample1)
    print(f"'{sample1}' -> '{result1}'")
    
    sample2 = "\t\t  Another test here"
    result2 = extract_first_word(sample2)
    print(f"'{sample2}' -> '{result2}'")
    
    sample3 = "   \n leading space"
    result3 = extract_first_word(sample3)
    print(f"'{sample3}' -> '{result3}'")
    
    sample4 = ""
    result4 = extract_first_word(sample4)
    print(f"'{sample4}' -> '{result4}'")