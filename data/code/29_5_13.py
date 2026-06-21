def count_vowels_generator():
    sentences = [
        "Hello world",
        "Python is great",
        "AI changes everything",
        "The quick brown fox",
        "Jumps over the lazy dog"
    ]
    vowels = set('aeiouAEIOU')
    for sentence in sentences:
        for word in sentence.split():
            vowel_count = sum(1 for char in word if char in vowels)
            yield (word, vowel_count)

if __name__ == '__main__':
    results = list(count_vowels_generator())
    print(results)