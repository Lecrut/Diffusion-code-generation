def check_term_in_sentences(term: str, sentences: list) -> bool:
    if not term or not isinstance(term, str):
        raise ValueError("Term must be a non-empty string")
    if not sentences or not all(isinstance(sentence, str) for sentence in sentences):
        raise ValueError("Sentences must be a list of non-empty strings")
    
    words_set = set(word for sentence in sentences for word in sentence.split())
    return term in words_set

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is an interpreted, high-level and general-purpose programming language"
    ]
    search_term = "interpreted"
    
    try:
        result = check_term_in_sentences(search_term, sample_sentences)
        print(f"Term '{search_term}' found in sentences: {result}")
    except ValueError as e:
        print(e)