class ContradictionDetector:

    def __init__(self):
        self.positive_keywords = {'must', 'should', 'need'}
        self.negative_keywords = {'cannot', 'should not', 'forbidden'}

    def detect_contradiction(self, statement1, statement2):
        keywords1 = self.extract_keywords(statement1)
        keywords2 = self.extract_keywords(statement2)
        positive_overlap = self.positive_keywords.intersection(keywords1) & self.positive_keywords.intersection(keywords2)
        negative_overlap = self.negative_keywords.intersection(keywords1) & self.negative_keywords.intersection(keywords2)
        return bool(positive_overlap and negative_overlap)

    def extract_keywords(self, statement):
        keywords = set()
        for word in statement.split():
            if word.lower() in self.positive_keywords or word.lower() in self.negative_keywords:
                keywords.add(word.lower())
        return keywords
if __name__ == '__main__':
    detector = ContradictionDetector()
    sample_statement1 = 'I must eat healthy food.'
    sample_statement2 = 'I cannot eat junk food.'
    result = detector.detect_contradiction(sample_statement1, sample_statement2)
    print(result)