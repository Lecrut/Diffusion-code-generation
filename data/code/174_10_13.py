CHARACTER_COUNT_THRESHOLD = 1

def count_character_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return {char: count for char, count in frequency_dict.items() if count >= CHARACTER_COUNT_THRESHOLD}

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_character_frequency(sample_string)
    print(result)