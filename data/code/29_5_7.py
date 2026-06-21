def count_vowels_per_word(sentences):
    for sentence in sentences:
        for word in sentence.split():
            clean_word = ''.join(c for c in word if c.isalpha())
            count = 0
            for char in clean_word.lower():
                if char in 'aeiou':
                    count += 1
            yield count

if __name__ == '__main__':
    sample_sentences = [
        "Hello world this is a test",
        "Python generator functions are memory efficient",
        "AEIOU aeiou are vowels"
    ]
    results = list(count_vowels_per_word(sample_sentences))
    print(results)