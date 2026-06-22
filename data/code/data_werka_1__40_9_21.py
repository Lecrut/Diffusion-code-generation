def extract_first_letters(strings):
    first_letters = []
    for s in strings:
        if s:
            first_letters.append(s[0])
    return first_letters

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "", "date"]
    print(extract_first_letters(sample_strings))