def reverse_word_order(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_word_order("Hello World"))
    print(reverse_word_order("Python is great"))
    print(reverse_word_order("One two three four"))