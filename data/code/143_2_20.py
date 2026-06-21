class ContradictionDetector:
    def __init__(self):
        self.statements = [
            "The sky is blue.",
            "The sun is bright."
        ]

    def analyze_statements(self, statements=None):
        if statements:
            self.statements = statements
        inverted_keywords = {}
        for statement in self.statements:
            words = statement.split()
            for word in words:
                if word not in inverted_keywords:
                    inverted_keywords[word] = 0
                inverted_keywords[word] += 1

        return inverted_keywords

if __name__ == '__main__':
    detector = ContradictionDetector()
    result = detector.analyze_statements()
    print(result)