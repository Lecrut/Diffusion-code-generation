class ContradictionDetector:
    def __init__(self, statement1: str, statement2: str):
        self.statement1 = statement1.lower()
        self.statement2 = statement2.lower()

    def detect_contradiction(self) -> bool:
        keywords_in_statement1 = set(self.statement1.split())
        keywords_in_statement2 = set(self.statement2.split())

        if keywords_in_statement1.intersection(keywords_in_statement2):
            return False
        else:
            return True

if __name__ == '__main__':
    detector = ContradictionDetector("I love cats", "I hate dogs")
    print(detector.detect_contradiction())