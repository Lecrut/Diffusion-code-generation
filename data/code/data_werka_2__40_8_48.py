def extract_initials(strings):
    initials = []
    for string in strings:
        if string:
            initials.append(string[0])
    return initials

if __name__ == '__main__':
    sample_strings = ['watermelon', 'xigua', 'yam', 'zucchini']
    initials = extract_initials(sample_strings)
    print(''.join(initials))