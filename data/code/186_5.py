def word_generator(word_list):
    sorted_list = sorted(word_list)
    for word in sorted_list:
        yield word
if __name__ == '__main__':
    input_words = ["banana", "apple", "cherry", "date"]
    generated_words = word_generator(input_words)
    result = list(generated_words)
    print(result)