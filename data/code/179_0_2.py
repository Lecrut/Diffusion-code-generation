import sys
def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
if __name__ == '__main__':
    sample_input = "this is a test string"
    result = reverse_word_order(sample_input)
    print(result)