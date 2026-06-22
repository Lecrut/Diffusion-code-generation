def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    lower_text = text.lower()
    count = 0
    for char in lower_text:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = count_consonants(sample_text)
    print(result)
    sample_text2 = "Python Programming"
    result2 = count_consonants(sample_text2)
    print(result2)