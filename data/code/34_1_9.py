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
    sample4 = "already Capitalized"
    sample5 = "word1 word2_with-hyphen"
    print(capitalize_first_letter_only(sample1))
    print(capitalize_first_letter_only(sample2))
    print(capitalize_first_letter_only(sample3))
    print(capitalize_first_letter_only(sample4))
    print(capitalize_first_letter_only(sample5))