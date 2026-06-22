def count_consonants(text):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    count = 0
    for char in text:
        if char.isalpha() and char.lower() in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_consonants(sample_text)
    print(result)