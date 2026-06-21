def generate_word_dict():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    word_dict = {i: words[idx] for i, idx in enumerate(indices)}
    return word_dict

if __name__ == '__main__':
    print(generate_word_dict())