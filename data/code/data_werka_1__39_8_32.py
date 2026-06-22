class SubstringMatcher:
    def __init__(self, text):
        self.text = text

    def find_matches(self, patterns):
        results = {}
        for pattern in patterns:
            matches = []
            for i in range(len(self.text) - len(pattern) + 1):
                substring = self.text[i:i + len(pattern)]
                if substring == pattern:
                    matches.append(substring)
            results[pattern] = matches
        return results

if __name__ == '__main__':
    sample_text = "abababa"
    sample_patterns = ["aba", "bab", "a", "b"]
    matcher = SubstringMatcher(sample_text)
    output = matcher.find_matches(sample_patterns)
    print(output)