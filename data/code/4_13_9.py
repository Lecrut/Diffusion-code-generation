def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonants = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') - vowels
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    sample_text = "Hello World!"
    print(count_consonants(sample_text))