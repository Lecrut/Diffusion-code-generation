def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for char in text if char.lower() in consonants)

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Python Programming"
    sample_text3 = "AEIOU"
    print(count_consonants(sample_text1))
    print(count_consonants(sample_text2))
    print(count_consonants(sample_text3))