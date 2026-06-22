def get_first_letter(s):
    EMPTY_STRING = ""
    return s[0] if s else EMPTY_STRING

if __name__ == '__main__':
    sample_values = ["Innovation", "", "Future", "Tech"]
    results = [get_first_letter(value) for value in sample_values]
    print(results)