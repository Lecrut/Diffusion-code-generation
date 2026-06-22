def capitalize_first_char(input_string):
    if not input_string:
        return ""
    return input_string[0].upper() + input_string[1:].lower()

if __name__ == '__main__':
    sample_text = "hELLO wORLD"
    result = capitalize_first_char(sample_text)
    print(result)