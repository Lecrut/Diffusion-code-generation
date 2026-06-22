def sort_words(input_string):
    words = input_string.split()
    return ' '.join(sorted(words))

if __name__ == '__main__':
    sample_input = "elderberry apple cherry banana date"
    sorted_string = sort_words(sample_input)
    print(sorted_string)