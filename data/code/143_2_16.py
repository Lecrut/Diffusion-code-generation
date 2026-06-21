class ContradictionDetector:
    def __init__(self):
        self.keywords = {
            'positive': ['good', 'great', 'excellent'],
            'negative': ['bad', 'terrible', 'horrible']
        }

    def detect_contradiction(self, statement1, statement2):
        for keyword in self.keywords['positive']:
            if keyword in statement1 and keyword in statement2:
                return True
        for keyword in self.keywords['negative']:
            if keyword in statement1 and keyword in statement2:
                return False
        return None

if __name__ == '__main__':
    detector = ContradictionDetector()
    result = detector.detect_contradiction('This is a great product.', 'I hate this product.')
    print(result)