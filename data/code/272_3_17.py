def sort_words(input_string):
    if not isinstance(input_string, str) or ' ' not in input_string:
        raise ValueError("Input must be a string containing space-separated words.")
    
    words = input_string.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

if __name__ == '__main__':
    sample_input = "apple banana cherry date elderberry"
    try:
        result = sort_words(sample_input)
        print(result)
    except ValueError as e:
        print(e)