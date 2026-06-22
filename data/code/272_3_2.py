def sort_words(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

if __name__ == '__main__':
    sample_input = "zebra apple mango banana cherry"
    result = sort_words(sample_input)
    print(result)