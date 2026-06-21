def reverse_word_order(input_string):
    if not input_string.strip():
        raise ValueError("Input cannot be empty.")
    
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_input = "hello world python programming"
    try:
        print("Original input:", sample_input)
        reversed_result = reverse_word_order(sample_input)
        print("Reversed word order:", reversed_result)
    except ValueError as e:
        print(e)

    empty_input = ""
    try:
        print("\nTesting with empty input:")
        print("Original input:", empty_input)
        result_empty = reverse_word_order(empty_input)
        print("Reversed word order:", result_empty)
    except ValueError as e:
        print(e)