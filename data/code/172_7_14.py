CODE_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

if __name__ == '__main__':
    sample_values = {1, 2, 3, 4, 5}
    print("Sample Values:")
    for value in sorted(sample_values):
        print(f"{value}: {CODE_MAP[value]}")