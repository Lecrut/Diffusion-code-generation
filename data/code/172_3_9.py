def generate_word_dict():
    words = ["apple", "banana", "cherry"]
    indices = sorted(range(len(words)), key=lambda x: words[x])
    word_dict = {index: words[index] for index in indices}
    return word_dict

if __name__ == '__main__':
    print(generate_word_dict())