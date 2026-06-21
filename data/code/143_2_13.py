class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            "positive": ["good", "great", "happy"],
            "negative": ["bad", "terrible", "sad"]
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword in self.keywords["positive"]:
            if keyword in statement1 and keyword in statement2:
                return True
        for keyword in self.keywords["negative"]:
            if keyword in statement1 and keyword in statement2:
                return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction("I am very happy", "I am feeling bad"))