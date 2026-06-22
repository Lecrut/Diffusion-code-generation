def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == '__main__':
    sample_string = "Programming is fun!"
    result = character_frequency(sample_string)
    print(f"Input: '{sample_string}'")
    print(f"Output: {result}")