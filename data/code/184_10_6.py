def find_keywords(text, keywords):
    word_counts = {}
    text_lower = text.lower()
    for keyword in keywords:
        keyword_lower = keyword.lower()
        if keyword_lower in text_lower:
            count = text_lower.count(keyword_lower)
            word_counts[keyword] = count
    return word_counts

if __name__ == '__main__':
    sample_text = "Python is a high-level, interpreted programming language."
    target_keywords = ["high-level", "interpreted", "language"]
    result = find_keywords(sample_text, target_keywords)
    print(result)