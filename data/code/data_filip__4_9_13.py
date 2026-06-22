import string

def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonant_set = set(string.ascii_letters) - vowels
    count = 0
    for char in text:
        if char in consonant_set:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, World! This is a performance test with 123456."
    result = count_consonants(sample_text)
    print(result)