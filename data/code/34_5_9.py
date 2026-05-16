def capitalize_first_letter_only(text):
    if not text:
        return ""
    result = ""
    capitalize_next = True
    for char in text:
        if capitalize_next and 'a' <= char <= 'z':
            result += char.upper()
            capitalize_next = False
        else:
            result += char
            if char.isalpha():
                capitalize_next = False
            elif char.isspace():
                capitalize_next = True
            else:
                capitalize_next = False
    return result
if __name__ == '__main__':
    sample1 = "this is a test string"
    sample2 = "hello world python"
    sample3 = "aBcDeFg"
    sample4 = "tHis iS a TeSt"
    sample5 = "  leading spaces and trailing ones  "
    sample6 = ""
    sample7 = "singleword"
    print(f"'{sample1}' -> '{capitalize_first_letter_only(sample1)}'")
    print(f"'{sample2}' -> '{capitalize_first_letter_only(sample2)}'")
    print(f"'{sample3}' -> '{capitalize_first_letter_only(sample3)}'")
    print(f"'{sample4}' -> '{capitalize_first_letter_only(sample4)}'")
    print(f"'{sample5}' -> '{capitalize_first_letter_only(sample5)}'")
    print(f"'{sample6}' -> '{capitalize_first_letter_only(sample6)}'")
    print(f"'{sample7}' -> '{capitalize_first_letter_only(sample7)}'")