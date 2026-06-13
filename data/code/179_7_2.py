def reverse_word_order(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
if __name__ == '__main__':
    sample_string = "the quick brown fox jumps over the lazy dog"
    result = reverse_word_order(sample_string)
    print(result)