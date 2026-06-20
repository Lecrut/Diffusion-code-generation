import string

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans("", "", vowels)
    return text.translate(trans_table)

if __name__ == '__main__':
    sample_text = "Hello World 123!"
    result = remove_vowels(sample_text)
    print(result)