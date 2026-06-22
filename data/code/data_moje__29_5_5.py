def vowel_counts_generator():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a versatile programming language",
        "Machine learning algorithms process large datasets"
    ]
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = sum(1 for char in word.lower() if char in 'aeiou')
            yield count

if __name__ == '__main__':
    results = list(vowel_counts_generator())
    print(results)