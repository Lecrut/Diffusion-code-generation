class SubstringExtractor:
    START_CHAR = 'a'
    END_CHAR = 'e'

    @staticmethod
    def extract_substrings(s, start=START_CHAR, end=END_CHAR):
        substrings = []
        for i in range(len(s)):
            if s[i] == start:
                for j in range(i + 1, len(s) + 1):
                    if s[j - 1] == end:
                        substrings.append(s[i:j])
        return substrings

if __name__ == '__main__':
    target_string = "abcdeabc"
    extractor = SubstringExtractor()
    result = SubstringExtractor.extract_substrings(target_string)
    print(result)