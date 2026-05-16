def capitalize_first_letter(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "a"
    sample3 = "python programming"
    sample4 = ""
    sample5 = "already Capitalized"
    print(f"'{sample1}' -> '{capitalize_first_letter(sample1)}'")
    print(f"'{sample2}' -> '{capitalize_first_letter(sample2)}'")
    print(f"'{sample3}' -> '{capitalize_first_letter(sample3)}'")
    print(f"'{sample4}' -> '{capitalize_first_letter(sample4)}'")
    print(f"'{sample5}' -> '{capitalize_first_letter(sample5)}'")
    try:
        capitalize_first_letter(123)
    except TypeError as e:
        print(f"Caught expected error: {e}")