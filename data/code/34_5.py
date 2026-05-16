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
    sample4 = "  leading spaces and trailing ones  "
    sample5 = ""
    sample6 = "singleword"
    print(f"Input: '{sample1}'\nOutput: '{capitalize_first_letter_only(sample1)}'")
    print("-" * 20)
    print(f"Input: '{sample2}'\nOutput: '{capitalize_first_letter_only(sample2)}'")
    print("-" * 20)
    print(f"Input: '{sample3}'\nOutput: '{capitalize_first_letter_only(sample3)}'")
    print("-" * 20)
    print(f"Input: '{sample4}'\nOutput: '{capitalize_first_letter_only(sample4)}'")
    print("-" * 20)
    print(f"Input: '{sample5}'\nOutput: '{capitalize_first_letter_only(sample5)}'")
    print("-" * 20)
    print(f"Input: '{sample6}'\nOutput: '{capitalize_first_letter_only(sample6)}'")