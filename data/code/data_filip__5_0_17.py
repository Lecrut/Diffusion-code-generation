def capitalize_first_char(text):
    if not text:
        return ""
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_1 = "hEllo wOrld"
    sample_2 = "tHiS is a TeSt"
    sample_3 = "a"
    sample_4 = "ALL CAPS"
    result_1 = capitalize_first_char(sample_1)
    result_2 = capitalize_first_char(sample_2)
    result_3 = capitalize_first_char(sample_3)
    result_4 = capitalize_first_char(sample_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)