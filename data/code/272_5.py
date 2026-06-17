def alphabetize_word_generator(word_list):
    sorted_words = sorted(word_list)
    for word in sorted_words:
        yield word
if __name__ == '__main__':
    sample_list = ["banana", "apple", "date", "cherry", "elderberry"]
    word_generator = alphabetize_word_generator(sample_list)
    result_list = list(word_generator)
    print(result_list)