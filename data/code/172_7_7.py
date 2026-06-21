CODE_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

if __name__ == '__main__':
    print("Code to Word Mapping:")
    for code, word in CODE_TO_WORD.items():
        print(f"{code}: {word}")