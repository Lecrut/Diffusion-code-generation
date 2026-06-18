def get_first_letters(sentence: str) -> list[str]:
    words = sentence.split()
    return [word[0] for word in words if len(word) > 0]
if __name__ == '__main__':
    sample_sentence = "Hello world this is a test script"
    result = get_first_letters(sample_sentence)
    print("".join(result))