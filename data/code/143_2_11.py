class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            'positive': ['good', 'great', 'excellent'],
            'negative': ['bad', 'terrible', 'horrible']
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword_group in self.keywords:
            if any(keyword in statement1.lower() for keyword in self.keywords[keyword_group]):
                if any(keyword in statement2.lower() for keyword in self.keywords[keyword_group]):
                    return True
        return False

if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_contradiction('This is a great product.', 'I do not like this product.'))