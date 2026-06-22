def sort_words(input_string):
    words = input_string.split()
    return ' '.join(sorted(words))

if __name__ == '__main__':
    sample_input = "zebra apple mango banana cherry"
    sorted_string = sort_words(sample_input)
    print(sorted_string)