def get_first_letter(s):
    if not s:
        return ""
    return s[0]

if __name__ == '__main__':
    sample_values = ["hello", "", "world", "Python"]
    for value in sample_values:
        print(get_first_letter(value))