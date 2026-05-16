def capitalize_first_letter(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample1 = "hello world"
    result1 = capitalize_first_letter(sample1)
    print(f"Original: '{sample1}'")
    print(f"Result: '{result1}'")
    sample2 = "python programming"
    result2 = capitalize_first_letter(sample2)
    print(f"Original: '{sample2}'")
    print(f"Result: '{result2}'")
    sample3 = "a"
    result3 = capitalize_first_letter(sample3)
    print(f"Original: '{sample3}'")
    print(f"Result: '{result3}'")
    sample4 = ""
    result4 = capitalize_first_letter(sample4)
    print(f"Original: '{sample4}'")
    print(f"Result: '{result4}'")
    sample5 = "already capitalized"
    result5 = capitalize_first_letter(sample5)
    print(f"Original: '{sample5}'")
    print(f"Result: '{result5}'")