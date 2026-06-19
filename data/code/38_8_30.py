def analyze_string(input_string):
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    unique_chars = {char for char, count in char_counts.items() if count == 1}
    repeated_chars = [char for char, count in char_counts.items() if count > 1]

    return unique_chars, repeated_chars

if __name__ == '__main__':
    sample_string = "alibaba"
    unique_characters, repeated_characters = analyze_string(sample_string)
    print("Unique Characters:", unique_characters)
    print("Repeated Characters:", repeated_characters)