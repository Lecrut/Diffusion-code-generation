def is_valid_input(input_string):
    return input_string.strip() != ""

def reverse_word_order(input_string):
    if not is_valid_input(input_string):
        raise ValueError("Input cannot be empty.")
    
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_input = "hello world python programming"
    print("Original input:", sample_input)
    try:
        reversed_result = reverse_word_order(sample_input)
        print("Reversed word order:", reversed_result)
    except ValueError as e:
        print(e)