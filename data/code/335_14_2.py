import time
class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Natural language processing is a fascinating field of study."
    start_time = time.perf_counter_ns()
    tokens = processor.tokenize(sample_sentence)
    end_time = time.perf_counter_ns()
    execution_time_ms = (end_time - start_time) / 1_000_000.0
    assert isinstance(tokens, list), "Tokenize must return a list"
    expected_tokens = sample_sentence.split()
    assert tokens == expected_tokens, f"Tokens mismatch: {tokens} != {expected_tokens}"
    print(f"Input sentence processed in {execution_time_ms:.4f} ms")
    exit(0)