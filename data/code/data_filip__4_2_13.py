VOWELS = set('aeiouAEIOU')

def count_consonants(text):
    count = 0
    for char in text:
        if char.isalpha() and char not in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)