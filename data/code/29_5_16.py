def vowel_count_generator(sentences):
    vowels = set("aeiouAEIOU")
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            yield count

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python is great",
        "A quick brown fox jumps"
    ]
    for count in vowel_count_generator(sample_sentences):
        print(count)