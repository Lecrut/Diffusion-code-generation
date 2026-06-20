def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonant_list = [char for char in text if char.isalpha() and char not in vowels]
    return len(consonant_list)

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_consonants(sample_text)
    print(result)