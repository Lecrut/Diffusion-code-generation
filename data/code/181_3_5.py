filter_vowels = lambda sentences: [''.join(filter(lambda word: any(vowel in word for vowel in 'aeiouAEIOU'), sentence.split())) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = ["Hello world", "Python programming is fun", "Filter vowels only"]
    print(filter_vowels(sample_sentences))