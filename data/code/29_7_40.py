def reverse_word(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

if __name__ == '__main__':
    sample_input_1 = "hello"
    reversed_output_1 = reverse_word(sample_input_1)
    print(reversed_output_1)

    sample_input_2 = "world"
    reversed_output_2 = reverse_word(sample_input_2)
    print(reversed_output_2)