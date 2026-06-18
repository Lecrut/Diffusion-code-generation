import sys
def get_first_letters(text: str) -> list[str]:
    return [word[0] for word in text.split() if word]
if __name__ == '__main__':
    sample_sentence = "Hello World This Is A Test"
    result = get_first_letters(sample_sentence)
    print("".join(result))