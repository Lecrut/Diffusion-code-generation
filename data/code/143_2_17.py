class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            "love": ["hate", "dislike"],
            "happy": ["sad", "unhappy"]
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword, inverses in self.keywords.items():
            if any(keyword in statement1.lower() for inverse in inverses) and any(inverse in statement2.lower() for inverse in inverses):
                return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    result = detector.detect_contradiction("I love cats", "I dislike dogs")
    print(result)