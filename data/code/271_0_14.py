def count_character_frequencies(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

if __name__ == '__main__':
    sample_string = "hello world!"
    print(count_character_frequencies(sample_string))