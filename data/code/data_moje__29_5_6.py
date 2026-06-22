def vowel_count_generator(sentences):
    vowels = set('aeiouAEIOU')
    for sentence in sentences:
        for word in sentence.split():
            count = sum(1 for char in word if char in vowels)
            yield count

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox",
        "jumps over the lazy dog",
        "Python is awesome"
    ]
    counts = list(vowel_count_generator(sample_sentences))
    print(counts)