def count_vowels_per_word(sentences):
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            clean_word = ''.join(char for char in word if char.isalpha())
            vowel_count = 0
            for char in clean_word.lower():
                if char in 'aeiou':
                    vowel_count += 1
            yield vowel_count

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python is a great language",
        "The quick brown fox jumps over the lazy dog"
    ]
    results = list(count_vowels_per_word(sample_sentences))
    print(results)