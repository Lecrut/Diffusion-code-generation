def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_strings = ["abcdef", "hello", "world"]
    for sample in sample_strings:
        print(has_unique_characters(sample))