CODE_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

if __name__ == '__main__':
    sample_values = {6: "six", 7: "seven"}
    CODE_MAP.update(sample_values)
    for code, word in CODE_MAP.items():
        print(f"{code}: {word}")