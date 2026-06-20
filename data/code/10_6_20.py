def reverse_word_order(text):
    return " ".join(text.split()[::-1])

if __name__ == '__main__':
    print(reverse_word_order("Hello world this is a test"))
    print(reverse_word_order("Python code is fun"))
    print(reverse_word_order("One two three"))