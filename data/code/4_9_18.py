import string

CHAR_TYPE_MAP = {char: 'vowel' for char in 'aeiouAEIOU'}
for char in string.ascii_letters:
    if char not in CHAR_TYPE_MAP:
        CHAR_TYPE_MAP[char] = 'consonant'

def count_consonants(text):
    count = 0
    for char in text:
        if CHAR_TYPE_MAP.get(char) == 'consonant':
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Programming is fun and powerful, yet complex!"
    result = count_consonants(sample_text)
    print(result)