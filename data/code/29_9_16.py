import string

VOWELS = set('aeiouAEIOU')
TRANS_TABLE = str.maketrans(dict.fromkeys(string.ascii_letters + string.digits + string.punctuation + string.whitespace, ''))

def count_vowels(text):
    cleaned = text.translate(TRANS_TABLE)
    count = 0
    for char in cleaned:
        if char in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    large_string = "Hello World! This is a large string with many vowels. " * 10000
    result = count_vowels(large_string)
    print(result)