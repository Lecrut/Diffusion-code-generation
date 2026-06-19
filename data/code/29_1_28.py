def reverse_word(word):
    return ''.join(reversed(word))

if __name__ == '__main__':
    input_string = "world"
    output_string = reverse_word(input_string)
    print(output_string)
    
    another_input = "Alibaba"
    another_output = reverse_word(another_input)
    print(another_output)