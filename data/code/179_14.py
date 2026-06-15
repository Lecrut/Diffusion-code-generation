import sys
def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
if __name__ == '__main__':
    sample_input = "hello world python programming"
    print("Original input:", sample_input)
    if not sample_input.strip():
        print("Error: Input cannot be empty.")
    else:
        reversed_result = reverse_word_order(sample_input)
        print("Reversed word order:", reversed_result)