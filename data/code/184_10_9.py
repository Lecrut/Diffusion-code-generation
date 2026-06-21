def check_keywords(sentences, keywords):
    results = {keyword: False for keyword in keywords}
    for sentence in sentences:
        for keyword in keywords:
            if keyword in sentence:
                results[keyword] = True
                break
    return results

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is an interpreted, high-level and general-purpose programming language",
        "Hello world"
    ]
    keywords_to_check = ["quick", "Python", "hello"]
    print(check_keywords(sample_sentences, keywords_to_check))