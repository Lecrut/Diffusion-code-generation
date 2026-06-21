def generate_word_dict(word_list):
    return {i: word for i, word in enumerate(sorted(word_list))}

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    print(generate_word_dict(sample_words))