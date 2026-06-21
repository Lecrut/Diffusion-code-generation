def find_letter_sequences(s):
    return set(''.join(g) for _, g in itertools.groupby(s, str.isalpha))

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет!"
    print(find_letter_sequences(sample_string))