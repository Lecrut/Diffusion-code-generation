def phrase_length(phrase: str) -> int:
    return len(phrase)

if __name__ == '__main__':
    print(phrase_length("Hello, World!"))
    print(phrase_length("Python"))
    print(phrase_length(""))
    print(phrase_length("a" * 1000000))