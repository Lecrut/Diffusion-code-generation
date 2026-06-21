CODE_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

if __name__ == '__main__':
    try:
        sample_input = 3
        if sample_input not in CODE_TO_WORD:
            raise ValueError(f"Invalid input {sample_input}. Valid inputs are {list(CODE_TO_WORD.keys())}")

        print(f"The word for code {sample_input} is: {CODE_TO_WORD[sample_input]}")
    except Exception as e:
        print(e)