def get_first_letter(s):
    if s:
        return s[0]
    else:
        return ""

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python", ""]
    results = [get_first_letter(value) for value in sample_values]
    print(results)