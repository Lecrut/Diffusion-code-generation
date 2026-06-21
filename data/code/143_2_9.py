class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            "positive": ["good", "great", "happy"],
            "negative": ["bad", "terrible", "sad"]
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword_group in self.keywords.values():
            if any(keyword in statement1.lower() for keyword in keyword_group) and \
               any(keyword in statement2.lower() for keyword in keyword_group):
                return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction("This is a great day.", "I feel terrible today."))