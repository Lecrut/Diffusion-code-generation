vowels = set('aeiouAEIOU')

filter_vowels = lambda sentence: ' '.join(word for word in sentence.split() if any(char in vowels for char in word))

if __name__ == '__main__':
    sentences = ["Hello world", "Python programming is fun"]
    result = [filter_vowels(sentence) for sentence in sentences]
    print(result)