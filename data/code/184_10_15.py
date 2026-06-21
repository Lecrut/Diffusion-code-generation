def check_keywords(sentences, keywords):
    return {keyword: any(keyword in sentence for sentence in sentences) for keyword in keywords}

if __name__ == '__main__':
    sample_sentences = [
        "Python is an interpreted, high-level and general-purpose programming language.",
        "It was created by Guido van Rossum and first released in 1991.",
        "Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    ]
    keywords = ["interpreted", "Guido", "Java"]
    print(check_keywords(sample_sentences, keywords))