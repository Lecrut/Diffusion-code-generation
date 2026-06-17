def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split()
if __name__ == '__main__':
    sample_sentences = [
        "  Python is great   ",
        "One two three",
        "",
        "  Multiple   spaces between words. "
    ]
    for test_input in sample_sentences:
        result = split_sentence(test_input)
        print(f"Input: {repr(test_input)}")
        print(f"Output: {result}")