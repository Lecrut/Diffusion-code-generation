def reverse_word_order(text):
    return ' '.join(reversed(text.split()))

if __name__ == '__main__':
    sample_text = 'Python is awesome'
    print(reverse_word_order(sample_text))