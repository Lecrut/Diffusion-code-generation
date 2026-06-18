import sys
def get_first_letters(text: str) -> list[str]:
    words = text.split()
    return [word[0] for word in words if word]
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    result = get_first_letters(sample_text)
    print("".join(result))