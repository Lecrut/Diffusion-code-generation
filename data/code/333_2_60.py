def get_first_letters(sentence: str) -> list[str]:
    words = sentence.split()
    return [word[0] for word in words if word]
if __name__ == '__main__':
    sample_sentence = "Hello World This Is A Test"
    result = get_first_letters(sample_sentence)
    print("".join(result))