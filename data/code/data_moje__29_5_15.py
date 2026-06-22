def vowel_counts():
    sentences = [
        "Hello world",
        "Python is fun",
        "The quick brown fox",
        "Jumps over the lazy dog"
    ]
    for sentence in sentences:
        for word in sentence.split():
            count = sum(1 for char in word.lower() if char in 'aeiou')
            yield count

if __name__ == '__main__':
    for count in vowel_counts():
        print(count)