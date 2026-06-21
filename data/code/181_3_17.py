filter_vowels = lambda sentences: [''.join(filter(lambda char: char.lower() in 'aeiou', word)) for sentence in sentences for word in sentence.split()]

if __name__ == '__main__':
    sample_sentences = ["Hello world", "Python programming is fun"]
    print(filter_vowels(sample_sentences))