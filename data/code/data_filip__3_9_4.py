def remove_vowels(s):
    trans_table = str.maketrans('', '', 'aeiouAEIOU')
    return s.translate(trans_table)

if __name__ == '__main__':
    sample = "Hello World"
    result = remove_vowels(sample)
    print(result)