def reverse_word_order(s):
    words = s.split()
    return " ".join(reversed(words))

if __name__ == '__main__':
    sample_string = "Data Science is fun"
    reversed_string = reverse_word_order(sample_string)
    print(reversed_string)