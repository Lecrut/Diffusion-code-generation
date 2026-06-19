def calculate_phrase_length(phrase: str) -> int:
    return len(phrase)

if __name__ == '__main__':
    SAMPLE_PHRASE_1 = "Hello, World!"
    SAMPLE_PHRASE_2 = "Python Programming"
    SAMPLE_PHRASE_3 = ""
    SAMPLE_PHRASE_4 = "a" * 1000000

    print(calculate_phrase_length(SAMPLE_PHRASE_1))
    print(calculate_phrase_length(SAMPLE_PHRASE_2))
    print(calculate_phrase_length(SAMPLE_PHRASE_3))
    print(calculate_phrase_length(SAMPLE_PHRASE_4))