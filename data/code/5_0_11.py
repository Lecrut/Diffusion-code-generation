def capitalize_first_char(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_1 = "hello world"
    sample_2 = "hELLO wORLD"
    sample_3 = ""
    sample_4 = "a"
    result_1 = capitalize_first_char(sample_1)
    result_2 = capitalize_first_char(sample_2)
    result_3 = capitalize_first_char(sample_3)
    result_4 = capitalize_first_char(sample_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)