def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    SAMPLE_VALUES = ["strawberry", "watermelon", "pineapple", "blueberry"]
    result = get_first_letters(SAMPLE_VALUES)
    print(result)