import sys
def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
if __name__ == '__main__':
    sample_input = "hello world python programming"
    if not sample_input:
        print("Error: Input cannot be empty.")
    else:
        result = reverse_word_order(sample_input)
        print(f"Original input: {sample_input}")
        print(f"Reversed word order: {result}")