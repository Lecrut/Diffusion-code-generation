def capitalize_first_lower_rest(text):
    if not text:
        return text
    return text[0].upper() + text[1:].lower()

if __name__ == '__main__':
    sample1 = "hELlo wORLD"
    sample2 = "PYTHON"
    sample3 = "javaScript"
    sample4 = ""
    sample5 = "a"
    print(capitalize_first_lower_rest(sample1))
    print(capitalize_first_lower_rest(sample2))
    print(capitalize_first_lower_rest(sample3))
    print(capitalize_first_lower_rest(sample4))
    print(capitalize_first_lower_rest(sample5))