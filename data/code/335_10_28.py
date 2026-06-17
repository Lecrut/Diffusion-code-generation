def split_sentence(text: str) -> list[str]:
    return text.split(' ')
if __name__ == '__main__':
    sample_text = "Hello world this is a test sentence"
    result_words = split_sentence(sample_text)
    print(result_words)