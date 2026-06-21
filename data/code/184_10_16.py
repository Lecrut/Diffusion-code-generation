def check_keyword_presence(sentences, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}
    sentences_lower = [sentence.lower() for sentence in sentences]
    for sentence in sentences_lower:
        for keyword in keywords:
            if keyword in sentence.split():
                keyword_counts[keyword] += sentence.count(keyword)
    return keyword_counts

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "A quick movement of the enemy will jeopardize six gunboats",
        "He jumped into the pool just as the others joined him."
    ]
    sample_keywords = ["quick", "fox", "dog", "cat"]
    result = check_keyword_presence(sample_sentences, sample_keywords)
    print(result)