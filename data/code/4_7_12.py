def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    lower_text = text.lower()
    for char in lower_text:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    result = count_consonants(sample_text)
    print(result)