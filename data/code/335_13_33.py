def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Python is a versatile programming language that excels in various domains."
    result_words = split_sentence(sample_sentence)
    print(f"Input: {sample_sentence}")
    print(f"Output ({len(result_words)} words):")
    for i, word in enumerate(result_words, start=1):
        print(f"{i}. '{word}'")