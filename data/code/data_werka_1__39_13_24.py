class SubstringExtractor:
    def __init__(self, s):
        self.s = s

    def extract(self, start, end):
        substrings = []
        for i in range(len(self.s)):
            if self.s[i] == start:
                for j in range(i + 1, len(self.s) + 1):
                    if self.s[j - 1] == end:
                        substrings.append(self.s[i:j])
        return substrings

if __name__ == '__main__':
    target_string = "abcdeabc"
    extractor = SubstringExtractor(target_string)
    start_point = 'a'
    end_point = 'e'
    result = extractor.extract(start_point, end_point)
    print(result)