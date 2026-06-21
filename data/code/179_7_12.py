def reverse_word_order(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_string = "Data Science is fun"
    reversed_string = reverse_word_order(sample_string)
    print(reversed_string)