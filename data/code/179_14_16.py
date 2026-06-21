def reverse_word_order(input_string):
    words = input_string.split()
    return " ".join(reversed(words))

if __name__ == '__main__':
    sample_input = "hello world python programming"
    print("Original input:", sample_input)
    reversed_result = reverse_word_order(sample_input.strip())
    print("Reversed word order:", reversed_result)