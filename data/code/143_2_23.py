class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            "happy": ["sad", "unhappy"],
            "love": ["hate", "dislike"],
            "win": ["lose", "defeat"]
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword, inverses in self.keywords.items():
            if any(keyword in statement1.lower() and inverse in statement2.lower() for inverse in inverses):
                return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction("I am happy", "I feel sad"))