class WordReverser:
    def reverse_word_order(self, input_string):
        words = input_string.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser = WordReverser()
    
    sample_input_1 = "hello world python programming"
    print("Original input:", sample_input_1)
    result_1 = reverser.reverse_word_order(sample_input_1)
    print("Reversed word order:", result_1)
    
    sample_input_2 = "this is a sample sentence"
    print("\nOriginal input:", sample_input_2)
    result_2 = reverser.reverse_word_order(sample_input_2)
    print("Reversed word order:", result_2)
    
    empty_input = ""
    print("\nTesting with empty input:")
    print("Original input:", empty_input)
    if not empty_input.strip():
        print("Error: Input cannot be empty.")