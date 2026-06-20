def reverse_word_order(text_input):
    token_list = text_input.split()
    reversed_list = list(reversed(token_list))
    output_string = ' '.join(reversed_list)
    return output_string

if __name__ == '__main__':
    test_phrase = "the quick brown fox jumps over the lazy dog"
    final_result = reverse_word_order(test_phrase)
    print(final_result)