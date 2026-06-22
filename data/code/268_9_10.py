def extract_and_strip_first_word(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    parts = text.split()
    if parts:
        return parts[0].strip()
    return ""

if __name__ == '__main__':
    sample1 = "  Hello world! "
    print(f"'{sample1}' -> '{extract_and_strip_first_word(sample1)}'")
    
    sample2 = "\t\t  Another test here\n"
    print(f"'{sample2}' -> '{extract_and_strip_first_word(sample2)}'")
    
    sample3 = "   \t"
    print(f"'{sample3}' -> '{extract_and_strip_first_word(sample3)}'")
    
    sample4 = "singleword"
    print(f"'{sample4}' -> '{extract_and_strip_first_word(sample4)}'")
    
    sample5 = ""
    print(f"'{sample5}' -> '{extract_and_strip_first_word(sample5)}'")