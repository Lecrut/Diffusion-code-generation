def sort_words(input_string):
    words = input_string.split()
    if not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a string of space-separated words")
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

if __name__ == '__main__':
    sample_input = "zebra apple mango banana cherry"
    result = sort_words(sample_input)
    print(result)