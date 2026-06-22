def find_most_frequent_chars(phrase):
    char_frequency = {}
    for char in phrase:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    max_frequency = max(char_frequency.values())
    most_frequent = [char for char, freq in char_frequency.items() if freq == max_frequency]
    
    return most_frequent

if __name__ == '__main__':
    sample_phrase = "character frequency test"
    result = find_most_frequent_chars(sample_phrase)
    print(result)