def sort_words(input_string):
    return ' '.join(sorted(input_string.split()))

if __name__ == '__main__':
    sample_input = "banana apple cherry"
    print(sort_words(sample_input))