def word_generator(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        yield word

if __name__ == '__main__':
    large_string = "This is a   sample string with various whitespace types.\nAnd some\ttabs and newlines."
    gen = word_generator(large_string)
    for _ in range(10):
        print(next(gen))