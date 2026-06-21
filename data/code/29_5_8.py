def vowel_counts(sentences):
    vowels = set('aeiouAEIOU')
    for sentence in sentences:
        for word in sentence.split():
            yield sum(1 for char in word if char in vowels)

if __name__ == '__main__':
    sentences = [
        "Hello World",
        "Python is fun",
        "OpenAI uses LLMs",
        "Count the vowels"
    ]
    for count in vowel_counts(sentences):
        print(count)