from collections import defaultdict

CHAR_FREQ_DICT = 'char_freq_dict'

def count_char_frequencies(input_string):
    freqs = defaultdict(int)
    for char in input_string:
        freqs[char] += 1
    return dict(freqs)

if __name__ == '__main__':
    sample_input = "hello world! welcome to the world of python."
    result = count_char_frequencies(sample_input)
    print(result)