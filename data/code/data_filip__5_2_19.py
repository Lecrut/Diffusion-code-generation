def capitalize_sentence(text):
    if not text:
        return text
    result = []
    first_alpha_found = False
    for char in text:
        if not first_alpha_found and char.isalpha():
            result.append(char.upper())
            first_alpha_found = True
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "hello world"
    capitalized = capitalize_sentence(sample_text)
    print(capitalized)
    sample_text_2 = "this is a test"
    capitalized_2 = capitalize_sentence(sample_text_2)
    print(capitalized_2)
    sample_text_3 = ""
    capitalized_3 = capitalize_sentence(sample_text_3)
    print(capitalized_3)
    sample_text_4 = "123abc"
    capitalized_4 = capitalize_sentence(sample_text_4)
    print(capitalized_4)