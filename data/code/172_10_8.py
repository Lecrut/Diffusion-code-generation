def int_to_word_map():
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

if __name__ == '__main__':
    mapping = int_to_word_map()
    for key, word in mapping.items():
        print(f"{key}: {word}")