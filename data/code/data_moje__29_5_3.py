def count_vowels_per_word(sentences):
    vowels = set('aeiouAEIOU')
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            yield count

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python is awesome",
        "Generator functions are memory efficient"
    ]
    results = list(count_vowels_per_word(sample_sentences))
    print(results)