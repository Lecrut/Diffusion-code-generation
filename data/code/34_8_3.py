def capitalize_first_letter(text: str) -> str:
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample1 = "hello world"
    result1 = capitalize_first_letter(sample1)
    print(f"Input: '{sample1}', Output: '{result1}'")
    sample2 = "python programming"
    result2 = capitalize_first_letter(sample2)
    print(f"Input: '{sample2}', Output: '{result2}'")
    sample3 = "a"
    result3 = capitalize_first_letter(sample3)
    print(f"Input: '{sample3}', Output: '{result3}'")
    sample4 = ""
    result4 = capitalize_first_letter(sample4)
    print(f"Input: '{sample4}', Output: '{result4}'")
    sample5 = "already capitalized"
    result5 = capitalize_first_letter(sample5)
    print(f"Input: '{sample5}', Output: '{result5}'")