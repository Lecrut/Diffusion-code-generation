def sorted_word_generator(word_list):
    sorted_list = sorted(word_list)
    for word in sorted_list:
        yield word
if __name__ == '__main__':
    input_words = ["banana", "apple", "cherry", "date"]
    word_generator = sorted_word_generator(input_words)
    result = list(word_generator)
    print(result)