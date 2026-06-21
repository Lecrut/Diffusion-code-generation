class ContradictionDetector:
    def __init__(self):
        self.sample_data = {
            "statement1": "The sky is blue.",
            "statement2": "The sky is not blue."
        }

    def detect_contradiction(self, statement1, statement2):
        inverted_statement1 = statement1.replace("not ", "")
        inverted_statement2 = statement2.replace("not ", "")
        return inverted_statement1 == inverted_statement2

if __name__ == '__main__':
    detector = ContradictionDetector()
    result = detector.detect_contradiction(detector.sample_data["statement1"], detector.sample_data["statement2"])
    print(result)