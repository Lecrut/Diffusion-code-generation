def find_unique_characters(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    unique_chars = []
    for char in input_string:
        if frequency[char] == 1:
            unique_chars.append(char)
    
    return unique_chars

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)