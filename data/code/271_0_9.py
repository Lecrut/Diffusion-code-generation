CHAR_FREQ = {}

def count_char_frequency(input_string):
    for char in input_string:
        if char in CHAR_FREQ:
            CHAR_FREQ[char] += 1
        else:
            CHAR_FREQ[char] = 1

if __name__ == '__main__':
    sample_string = "hello world"
    count_char_frequency(sample_string)
    print(CHAR_FREQ)