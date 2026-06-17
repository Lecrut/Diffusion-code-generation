import re
class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello   world", "Python is great  ", "", "One Two Three"]
    results = []
    input_strs = list(sample_sentences)
    for i, s in enumerate(input_strs):
        result_list = processor.split_sentence(s)
        print(f"Input: '{s}'")
        print(f"Output: {result_list}")
        if not isinstance(result_list, list):
            exit(1)