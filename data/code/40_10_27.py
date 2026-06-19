def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_strings = ["kiwi", "mango", "papaya", "grape", ""]
    result = get_first_letters(sample_strings)
    print(result)