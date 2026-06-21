def check_term_in_sentences(sentences: list, term: str) -> bool:
    for sentence in sentences:
        if term in sentence.split():
            return True
    return False

if __name__ == '__main__':
    sample_sentences = ["The quick brown fox jumps over the lazy dog", 
                       "Lorem ipsum dolor sit amet", 
                       "Python is an interpreted, high-level and general-purpose programming language"]
    search_term = "fox"
    print(f"Sentences: {sample_sentences}")
    print(f"Search Term: '{search_term}'")
    result = check_term_in_sentences(sample_sentences, search_term)
    print(f"Term found in sentences: {result}")