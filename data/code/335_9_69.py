import re
def split_words_pythonic(text: str) -> list[str]:
    return [word for word in text.split()]
if __name__ == '__main__':
    sample_text = "  Hello World Python Programming is Fun!  "
    words = split_words_pythonic(sample_text.lower().replace("!", ""))
    if len(words) > 0:
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")