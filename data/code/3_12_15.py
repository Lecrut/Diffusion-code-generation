def remove_vowels(s):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans("", "", vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    sample_text = "Hello World, this is a Test String with Vowels."
    result = remove_vowels(sample_text)
    print(result)