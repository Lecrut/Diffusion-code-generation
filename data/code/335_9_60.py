def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Python is awesome! Data science and AI are the future."
    words = split_words(sample_text)
    for i, word in enumerate(words):
        print(f"{i + 1}: {word}")