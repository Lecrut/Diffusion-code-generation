def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_strings = ["hello", "world", "python", "abcdef"]
    results = [has_unique_characters(s) for s in test_strings]
    for s, result in zip(test_strings, results):
        print(f"{s}: {result}")