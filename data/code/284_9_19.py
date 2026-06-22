def reverse_each_word(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Data structures and algorithms"
    result = reverse_each_word(sample_input)
    print(result)