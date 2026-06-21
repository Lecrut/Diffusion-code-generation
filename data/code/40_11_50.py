def get_first_letter(s):
    EMPTY_STRING = ""
    if not s:
        return EMPTY_STRING
    return s[0]

if __name__ == '__main__':
    SAMPLE_VALUES = ["Hello", "", "World", "Python"]
    RESULTS = [get_first_letter(value) for value in SAMPLE_VALUES]
    print(RESULTS)