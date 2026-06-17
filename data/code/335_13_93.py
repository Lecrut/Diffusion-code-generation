def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split()
if __name__ == '__main__':
    sample_sentence = "  Hello, World! This is a test string with multiple   spaces and punctuation."
    result_words = split_sentence(sample_sentence)
    print("Sample Sentence:")
    print(f'"{sample_sentence}"')
    print("\nSplit Words:")
    for i, word in enumerate(result_words):
        if i > 0:
            print("-" * (len(word)))
        else:
            print("")