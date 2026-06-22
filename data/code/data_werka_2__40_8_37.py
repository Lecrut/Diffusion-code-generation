def extract_first_letters(strings):
    first_letters = []
    for string in strings:
        if string:
            first_letters.append(string[0])
    return first_letters

if __name__ == '__main__':
    sample_strings = ['watermelon', 'xigua', 'yam', 'zucchini']
    result = extract_first_letters(sample_strings)
    print(result)