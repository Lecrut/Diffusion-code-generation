def vowel_counts(sentence_list):
    vowels = set('aeiouAEIOU')
    for sentence in sentence_list:
        for word in sentence.split():
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            yield count

if __name__ == '__main__':
    sentences = [
        "Hello World",
        "Python is awesome",
        "Generator functions are efficient",
        "No comments allowed here"
    ]
    for count in vowel_counts(sentences):
        print(count)