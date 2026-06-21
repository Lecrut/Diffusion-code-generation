def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_character_frequency(sample_string)
    print(result)