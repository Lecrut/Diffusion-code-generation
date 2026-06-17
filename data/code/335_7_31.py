def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    return [word.strip('.,!?;:') for word in words]
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    result = split_sentence(sample_text)
    print(result)