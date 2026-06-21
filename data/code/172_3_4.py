def generate_word_dict(words):
    return {i: word for i, word in enumerate(sorted(words))}

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    print(generate_word_dict(sample_words))