def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonants_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for char in text if char in consonants_set)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)