def get_first_letter(s):
    if not s:
        return ""
    first_char = s[0]
    return first_char

if __name__ == '__main__':
    sample_values = ["Example", "", "Test", "String"]
    results = [get_first_letter(value) for value in sample_values]
    print(results)