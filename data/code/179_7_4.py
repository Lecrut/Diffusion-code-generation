def reverse_word_order(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    input_string = "the quick brown fox"
    result = reverse_word_order(input_string)
    print(result)