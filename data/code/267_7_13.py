def is_long_word(word: str) -> bool:
    return len(word) > 10

if __name__ == '__main__':
    print(is_long_word("example"))
    print(is_long_word("examples"))