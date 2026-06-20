def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonants = [char for char in text if char.isalpha() and char not in vowels]
    return len(consonants)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    result = count_consonants(sample_text)
    print(result)