def vowel_counts():
    sentences = [
        "Hello World",
        "OpenAI",
        "Python Programming",
        "Count the vowels here",
        "AEIOU and aeiou"
    ]
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = sum(1 for char in word.lower() if char in 'aeiou')
            yield count

if __name__ == '__main__':
    for count in vowel_counts():
        print(count)