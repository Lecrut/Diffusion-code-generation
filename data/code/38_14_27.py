from collections import Counter

def find_repeated_characters(input_string):
    char_count = Counter(input_string)
    repeated_chars = [char for char, count in char_count.items() if count > 1]
    return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = "example string with some repeated letters"
    result = find_repeated_characters(sample_string)
    print(result)