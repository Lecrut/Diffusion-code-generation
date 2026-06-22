def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result
if __name__ == '__main__':
    sample_inputs = ['Hello World', 'Python is awesome', 'Reverse this sentence', 'SingleWord', '  Multiple   spaces   here  ']
    for sample in sample_inputs:
        result = reverse_word_order(sample)
        print(f"Original: '{sample}' -> Reversed: '{result}'")