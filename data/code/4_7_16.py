def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in text.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = count_consonants(sample_text)
    print(result)