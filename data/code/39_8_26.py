class SubstringMatcher:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def find_substrings(text, pattern):
        matches = []
        for i in range(len(text) - len(pattern) + 1):
            substring = text[i:i + len(pattern)]
            if substring == pattern:
                matches.append(substring)
        return matches

    def match_patterns(self, patterns):
        results = {}
        for pattern in patterns:
            results[pattern] = SubstringMatcher.find_substrings(self.text, pattern)
        return results

if __name__ == '__main__':
    sample_text = "abababa"
    sample_patterns = ["aba", "bab", "a", "b"]
    matcher = SubstringMatcher(sample_text)
    output = matcher.match_patterns(sample_patterns)
    print(output)