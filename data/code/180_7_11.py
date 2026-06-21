def check_term_in_sentences(sentences, term):
    term_set = set(term.split())
    for sentence in sentences:
        if term_set.issubset(set(sentence.split())):
            return True
    return False

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "A stitch in time saves nine",
        "Every cloud has a silver lining"
    ]
    term_to_check = "quick fox"
    result = check_term_in_sentences(sample_sentences, term_to_check)
    print(result)