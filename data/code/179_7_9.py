def reverse_word_order(s):
    return " ".join(s.split()[::-1])

if __name__ == '__main__':
    sample_string = "Data Science is fun"
    reversed_string = reverse_word_order(sample_string)
    print(reversed_string)