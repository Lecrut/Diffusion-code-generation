import string

def strip_vowels(text):
    vowels = 'aeiouAEIOU'
    trans_table = str.maketrans('', '', vowels)
    return text.translate(trans_table)
if __name__ == '__main__':
    sample_text = 'Hello World! How are you?'
    result = strip_vowels(sample_text)
    print(result)