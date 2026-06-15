import sys
def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
if __name__ == '__main__':
    sample_input = "this is a sample sentence"
    print("Original input:", sample_input)
    result = reverse_word_order(sample_input)
    print("Reversed word order:", result)
    empty_input = ""
    print("\nTesting with empty input:")
    print("Original input:", empty_input)
    if not empty_input:
        print("Error: Input cannot be empty.")
    else:
        result_empty = reverse_word_order(empty_input)
        print("Reversed word order:", result_empty)