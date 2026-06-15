def reverse_word_order(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    sample_string = "hello world this is a test"
    reversed_string = reverse_word_order(sample_string)
    print(reversed_string)