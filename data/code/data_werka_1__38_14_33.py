def find_repeated_characters(input_string):
    from collections import defaultdict
    char_frequency = defaultdict(int)
    for char in input_string:
        char_frequency[char] += 1
    repeated_chars = [char for char, count in char_frequency.items() if count > 1]
    return sorted(repeated_chars)
if __name__ == '__main__':
    sample_string = 'data structures'
    result = find_repeated_characters(sample_string)
    print(result)