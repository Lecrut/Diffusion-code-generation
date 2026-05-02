import collections
def find_repeated_characters(input_string):
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeated_chars = []
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars.append(char)
    return repeated_chars
if __name__ == '__main__':
    sample_string = "programming"
    repeated = find_repeated_characters(sample_string)
    print(repeated)