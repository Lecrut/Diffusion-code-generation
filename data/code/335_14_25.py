import timeit
class NlpProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NlpProcessor()
    sample_sentence = "Natural Language Processing is a fascinating field."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)
    assert isinstance(tokens, list), "Output must be a list"
    assert len(tokens) > 0, "Input sentence was empty or invalid"
    for token in tokens:
        assert isinstance(token, str), f"All elements must be strings. Found {type(token)}."
    setup_code = 'from __main__ import NlpProcessor; p = NlpProcessor()'
    stmt = "p.tokenize('This is a performance test for the tokenize method.') * 10"
    result_time = timeit.timeit(stmt, setup=setup_code, number=1)
    print(f"Tokenization benchmark completed in {result_time:.4f} seconds")