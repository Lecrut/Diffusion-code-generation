def count_word_frequency(text):
    word_count = {}
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    result = count_word_frequency(sample_text)
    print(result)