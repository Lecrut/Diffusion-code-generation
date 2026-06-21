def create_indexed_word_dict():
    words = ["dog", "cat", "elephant", "ant"]
    sorted_indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    indexed_words = {i: words[idx] for idx, i in enumerate(sorted_indices)}
    return indexed_words

if __name__ == '__main__':
    result_dict = create_indexed_word_dict()
    print(result_dict)