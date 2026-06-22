def vowel_counts(sentences):
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = 0
            for char in word.lower():
                if char in 'aeiou':
                    count += 1
            yield count

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python is great",
        "A quick brown fox",
        "The lazy dog"
    ]
    results = list(vowel_counts(sample_sentences))
    print(results)