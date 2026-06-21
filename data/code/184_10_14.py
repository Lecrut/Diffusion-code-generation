def find_keywords(sentences, keywords):
    return {keyword: any(keyword in sentence for sentence in sentences) for keyword in keywords}

if __name__ == '__main__':
    sample_sentences = [
        "Python is a versatile programming language.",
        "It supports multiple programming paradigms.",
        "Python is widely used for web development."
    ]
    sample_keywords = ["Python", "Java", "JavaScript"]
    print(find_keywords(sample_sentences, sample_keywords))