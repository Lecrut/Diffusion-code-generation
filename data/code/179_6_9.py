def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
if __name__ == '__main__':
    sample_text = 'Python is awesome'
    result = reverse_words(sample_text)
    print(result)