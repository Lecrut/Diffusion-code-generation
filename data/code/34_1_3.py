def capitalize_first_letter_only(text):
    result = []
    capitalize_next = True
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char.lower())
        else:
            result.append(char)
            if char.isspace():
                capitalize_next = True
            else:
                capitalize_next = False
    return "".join(result)
if __name__ == '__main__':
    sample1 = "hello world this is a test"
    sample2 = "this is another example"
    sample3 = "a short sentence"
    sample4 = "tHis Is A TeSt"
    sample5 = "  leading and trailing spaces "
    sample6 = ""
    print(f"'{sample1}' -> '{capitalize_first_letter_only(sample1)}'")
    print(f"'{sample2}' -> '{capitalize_first_letter_only(sample2)}'")
    print(f"'{sample3}' -> '{capitalize_first_letter_only(sample3)}'")
    print(f"'{sample4}' -> '{capitalize_first_letter_only(sample4)}'")
    print(f"'{sample5}' -> '{capitalize_first_letter_only(sample5)}'")
    print(f"'{sample6}' -> '{capitalize_first_letter_only(sample6)}'")