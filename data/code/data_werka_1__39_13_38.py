class SubstringExtractor:
    def __init__(self, s):
        self.s = s

    @staticmethod
    def find_indices(s, char):
        return [i for i, c in enumerate(s) if c == char]

    def extract(self, start, end):
        start_indices = self.find_indices(self.s, start)
        end_indices = self.find_indices(self.s, end)
        substrings = [
            self.s[s_index:e_index + 1]
            for s_index in start_indices
            for e_index in end_indices
            if s_index < e_index
        ]
        return substrings

if __name__ == '__main__':
    target_string = "abcdeabc"
    extractor = SubstringExtractor(target_string)
    start_point = 'a'
    end_point = 'e'
    result = extractor.extract(start_point, end_point)
    print(result)