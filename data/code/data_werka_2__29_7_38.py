def reverse_word(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

if __name__ == '__main__':
    sample_input = "world"
    reversed_output = reverse_word(sample_input)
    print(reversed_output)