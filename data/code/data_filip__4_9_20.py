def count_consonants(text):
    vowels = set('aeiouAEIOU')
    alpha_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    consonants = alpha_chars - vowels
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    text = "Hello World"
    result = count_consonants(text)
    print(result)