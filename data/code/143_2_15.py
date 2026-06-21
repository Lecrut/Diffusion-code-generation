class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            "positive": ["good", "great", "excellent"],
            "negative": ["bad", "terrible", "horrible"]
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword_type, keywords in self.keywords.items():
            if any(keyword in statement1.lower() for keyword in keywords) and \
               any(keyword in statement2.lower() for keyword in keywords):
                return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction("This is a great product.", "I hate this product."))