def capitalize_first_lower_rest(s):
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    test_strings = ["hELLO", "wOrld", "PYTHON", "a", "", "tEsT CaSe"]
    for text in test_strings:
        result = capitalize_first_lower_rest(text)
        print(result)