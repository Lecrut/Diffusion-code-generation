def vowel_count_generator():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a powerful programming language",
        "Generators save memory by yielding one item at a time",
        "Every word should be counted accurately",
        "Hello world this is a test"
    ]
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = 0
            for char in word.lower():
                if char in 'aeiou':
                    count += 1
            yield count

if __name__ == '__main__':
    result = list(vowel_count_generator())
    print(result)