def vowel_counts(sentences):
    vowels = set("aeiouAEIOU")
    for sentence in sentences:
        for word in sentence.split():
            count = sum(1 for char in word if char in vowels)
            yield count

if __name__ == '__main__':
    sentences = [
        "Hello World",
        "Python is great",
        "Count the vowels here"
    ]
    for count in vowel_counts(sentences):
        print(count)