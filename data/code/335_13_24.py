def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentences = [
        "Hello, world! This is a test.",
        "Python 3.10 is great for data science tasks."
    ]
    results = []
    for s in sample_sentences:
        words = split_sentence(s)
        results.append(words)
    print(results)