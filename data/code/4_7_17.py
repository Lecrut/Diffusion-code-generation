def count_consonants(text):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    return sum(1 for char in text.lower() if char.isalpha() and char in consonants)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)