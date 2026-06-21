filter_vowels = lambda sentences: [''.join(filter(lambda word: any(vowel in word for vowel in 'aeiou'), sentence.split())) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = ["Hello world", "Python programming is fun"]
    print(filter_vowels(sample_sentences))