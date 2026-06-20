def capitalize_first_letter(text):
    if not text:
        return text
    if len(text) == 1:
        return text.upper()
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_1 = "hELLO wORLD"
    sample_2 = "python"
    sample_3 = "123abc"
    sample_4 = ""
    result_1 = capitalize_first_letter(sample_1)
    result_2 = capitalize_first_letter(sample_2)
    result_3 = capitalize_first_letter(sample_3)
    result_4 = capitalize_first_letter(sample_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)