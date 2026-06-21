def check_term_in_sentences(sentences: list, term: str) -> bool:
    term_set = set(term.lower() for term in sentences)
    return term.lower() in term_set

if __name__ == '__main__':
    sample_sentences = ["Python is great", "Java is also great", "Python is versatile"]
    search_term = "python"
    result = check_term_in_sentences(sample_sentences, search_term)
    print(f"Term found: {result}")