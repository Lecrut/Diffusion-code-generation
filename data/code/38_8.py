import collections
def find_repeated_characters(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = []
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars.append(char)
    return repeated_chars
if __name__ == '__main__':
    sample_string = "programming"
    repeated = find_repeated_characters(sample_string)
    print(repeated)