def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    print(reverse_word_order("Hello world this is a test"))
    print(reverse_word_order("Python code generation works"))
    print(reverse_word_order("Reverse the order of words"))