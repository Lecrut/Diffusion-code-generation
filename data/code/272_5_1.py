def alphabetize_words(word_list):
    sorted_list = sorted(word_list)
    for word in sorted_list:
        yield word
if __name__ == '__main__':
    sample_list = ["banana", "apple", "date", "cherry", "elderberry"]
    word_generator = alphabetize_words(sample_list)
    result = list(word_generator)
    print(result)