def count_consonants(text):
    VOWELS = set('aeiouAEIOU')
    total = len(text)
    vowels = sum(1 for char in text if char in VOWELS)
    non_alpha = sum(1 for char in text if not char.isalpha())
    consonants = total - vowels - non_alpha
    return consonants

if __name__ == '__main__':
    text = 'Hello, World!'
    result = count_consonants(text)
    print(result)