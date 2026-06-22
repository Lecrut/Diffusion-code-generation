def sort_words(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

if __name__ == '__main__':
    sample_input = "apple banana cherry date elderberry"
    sorted_string = sort_words(sample_input)
    print(sorted_string)