def count_consonants(text):
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count
if __name__ == '__main__':
    sample_texts = ['Hello World', 'Python Programming', 'AEIOU', 'bcd', '', '12345!@#$%', 'A quick brown fox jumps over the lazy dog']
    for text in sample_texts:
        result = count_consonants(text)
        print(f"Consonants in '{text}': {result}")