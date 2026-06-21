vowels = "aeiouAEIOU"
contains_vowel = lambda word: any(char in vowels for char in word)
filter_words_with_vowels = lambda sentences: [' '.join(filter(contains_vowel, sentence.split())) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences1 = ["Hello World", "Programming is fun"]
    result1 = filter_words_with_vowels(sample_sentences1)
    print(f"Sentences with vowels: {result1}")