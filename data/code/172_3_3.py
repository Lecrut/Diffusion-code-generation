def generate_word_dict():
    words = ["apple", "banana", "cherry"]
    indices = sorted(range(len(words)), key=lambda i: len(words[i]))
    word_dict = {i: words[idx] for idx, i in enumerate(indices)}
    return word_dict

if __name__ == '__main__':
    print(generate_word_dict())