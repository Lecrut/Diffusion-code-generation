def sort_words(input_string):
    words = input_string.split()
    return ' '.join(sorted(words))

if __name__ == '__main__':
    sample_input = "zebra apple mango banana cherry"
    if not isinstance(sample_input, str) or not all(char.isalnum() or char.isspace() for char in sample_input):
        raise ValueError("Input must be a string of space-separated words")
    result = sort_words(sample_input)
    print(result)