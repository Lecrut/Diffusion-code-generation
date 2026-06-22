class SubstringExtractor:
    def __init__(self, target_string):
        self.target_string = target_string

    def extract_unique_substrings(self, k: int) -> set:
        if not isinstance(k, int):
            raise ValueError("The length of the substring must be an integer.")
        if k <= 0 or k > len(self.target_string):
            raise ValueError("Invalid substring length.")
        
        unique_substrings = set()
        for i in range(len(self.target_string) - k + 1):
            substring = self.target_string[i:i+k]
            unique_substrings.add(substring)
        return unique_substrings

if __name__ == '__main__':
    try:
        extractor = SubstringExtractor("banana")
        target_length = 2
        result = extractor.extract_unique_substrings(target_length)
        print(result)
    except ValueError as e:
        print(e)