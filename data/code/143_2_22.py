class ContradictionDetector:
    def __init__(self):
        self.sample_data = {
            "statement1": "The sky is blue.",
            "statement2": "The sky is not blue."
        }

    def detect_contradiction(self, statement1, statement2):
        inverted_statement1 = self.invert_keywords(statement1)
        inverted_statement2 = self.invert_keywords(statement2)
        return inverted_statement1 == inverted_statement2

    def invert_keywords(self, statement):
        keywords = ["blue", "not blue"]
        for keyword in keywords:
            statement = statement.replace(keyword, f"not {keyword}" if keyword != "not blue" else "blue")
        return statement

if __name__ == '__main__':
    detector = ContradictionDetector()
    result = detector.detect_contradiction(detector.sample_data["statement1"], detector.sample_data["statement2"])
    print(result)