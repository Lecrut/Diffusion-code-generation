WORDS = ["apple", "banana", "cherry"]
SORT_KEY = lambda x: len(x)

def generate_word_dict(words=WORDS, sort_key=SORT_KEY):
    sorted_indices = sorted(range(len(words)), key=lambda idx: sort_key(words[idx]))
    word_dict = {i: words[idx] for i, idx in enumerate(sorted_indices)}
    return word_dict

if __name__ == '__main__':
    print(generate_word_dict())