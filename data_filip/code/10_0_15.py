def reverse_words(text):
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    sample = "Hello World from Python"
    result = reverse_words(sample)
    print(result)