def count_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    text = "Hello World"
    result = count_consonants(text)
    print(result)