def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Python is great for data science"
    result = split_words(sample_text)
    print(result)