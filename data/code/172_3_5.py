def generate_word_dict():
    words = ["apple", "banana", "cherry"]
    indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    return {i: words[idx] for i, idx in enumerate(indices)}

if __name__ == '__main__':
    print(generate_word_dict())