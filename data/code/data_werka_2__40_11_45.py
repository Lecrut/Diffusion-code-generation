def get_first_letter(s):
    if not s:
        return ""
    return s[0]

if __name__ == '__main__':
    sample_values = ["Hello", "", "World!", "Python"]
    for value in sample_values:
        print(get_first_letter(value))