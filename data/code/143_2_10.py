class ContradictionDetector:
    def __init__(self):
        self.sample_data = {
            "statement1": "The sky is blue.",
            "statement2": "The sky is green."
        }

    def detect_contradiction(self, statement1, statement2):
        keywords1 = set(statement1.lower().split())
        keywords2 = set(statement2.lower().split())

        inverted_keywords1 = {keyword for keyword in keywords1 if 'not' in keyword}
        inverted_keywords2 = {keyword for keyword in keywords2 if 'not' in keyword}

        return not (inverted_keywords1.isdisjoint(inverted_keywords2))

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction(detector.sample_data["statement1"], detector.sample_data["statement2"]))