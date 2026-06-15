def count_letter_frequency(input_string):
    frequency = {}
    for char in input_string:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            if lower_char in frequency:
                frequency[lower_char] += 1
            else:
                frequency[lower_char] = 1
    return frequency
if __name__ == '__main__':
    sample_string = "Hello World"
    result = count_letter_frequency(sample_string)
    print(result)