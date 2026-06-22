def vowel_counts():
    sentences = [
        "Hello World",
        "Python is great",
        "OpenAI builds models",
        "Count the vowels here"
    ]
    for sentence in sentences:
        for word in sentence.split():
            count = sum(1 for char in word.lower() if char in 'aeiou')
            yield count

if __name__ == '__main__':
    result = list(vowel_counts())
    print(result)