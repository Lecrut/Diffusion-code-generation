def check_keywords(sentences, keywords):
    keyword_set = set(keywords)
    results = {sentence: any(keyword in sentence for keyword in keyword_set) for sentence in sentences}
    return results

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is an interpreted, high-level and general-purpose programming language",
        "Hello world"
    ]
    sample_keywords = ["python", "hello"]
    print(check_keywords(sample_sentences, sample_keywords))