def sort_words(input_string):
    words = input_string.split()
    return ' '.join(sorted(words))

if __name__ == '__main__':
    sample_input = "apple banana cherry date elderberry"
    sorted_output = sort_words(sample_input)
    print(sorted_output)