def reverse_word(s):
    reversed_chars = [s[i] for i in range(len(s)-1, -1, -1)]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_input = "Alibaba"
    reversed_output = reverse_word(sample_input)
    print(reversed_output)