def capitalize_first_letter(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "python programming"
    sample3 = "a"
    sample4 = ""
    sample5 = "tEST"
    print(f"Original: '{sample1}' -> Capitalized: '{capitalize_first_letter(sample1)}'")
    print(f"Original: '{sample2}' -> Capitalized: '{capitalize_first_letter(sample2)}'")
    print(f"Original: '{sample3}' -> Capitalized: '{capitalize_first_letter(sample3)}'")
    print(f"Original: '{sample4}' -> Capitalized: '{capitalize_first_letter(sample4)}'")
    print(f"Original: '{sample5}' -> Capitalized: '{capitalize_first_letter(sample5)}'")