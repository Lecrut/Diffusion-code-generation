def print_first_letters(strings):
    for string in strings:
        if string:
            yield string[0]

if __name__ == '__main__':
    sample_strings = ['watermelon', 'xigua', 'yam', 'zucchini']
    for first_letter in print_first_letters(sample_strings):
        print(first_letter)