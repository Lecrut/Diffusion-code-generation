class SubstringExtractor:
    def __init__(self, phrase):
        self.phrase = phrase

    def extract_substrings(self, indices):
        extracted_substrings = []
        for index in indices:
            if 0 <= index < len(self.phrase):
                start = index
                end = index + 1
                substring = self.phrase[start:end]
                extracted_substrings.append(substring)
            else:
                print(f"Error: Invalid index {index}. Index must be within the bounds of the phrase.")
        return extracted_substrings

if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    extractor = SubstringExtractor(sample_phrase)
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to check: {sample_indices}")
    results = extractor.extract_substrings(sample_indices)
    for part in results:
        print(part)