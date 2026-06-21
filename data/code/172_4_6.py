def constant_to_word_mapping():
    return {
        "ONE": "one",
        "TWO": "two",
        "THREE": "three"
    }

if __name__ == '__main__':
    mapping = constant_to_word_mapping()
    print(mapping["ONE"])
    print(mapping["TWO"])
    print(mapping["THREE"])