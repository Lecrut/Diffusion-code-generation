def extract_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    SAMPLE_STRINGS = ['watermelon', 'xigua', 'yellow watermelon', 'zucchini']
    first_letters = extract_first_letters(SAMPLE_STRINGS)
    print(first_letters)