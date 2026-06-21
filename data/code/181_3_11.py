vowels = set("aeiouAEIOU")

filter_vowels = lambda sentence: ''.join(filter(lambda char: char in vowels, sentence))

if __name__ == '__main__':
    sample_texts = ["Hello World", "Programming is fun", "AEIOUaeiou123"]
    results = [filter_vowels(text) for text in sample_texts]
    print(results)