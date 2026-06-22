def reverse_word(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_input = "Python"
    reversed_output = reverse_word(sample_input)
    print(reversed_output)