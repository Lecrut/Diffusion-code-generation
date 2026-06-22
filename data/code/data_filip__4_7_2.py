def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in text:
        if char.lower() in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(count_consonants(sample_text))