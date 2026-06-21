def count_character_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_character_frequency(sample_string)
    print(result)