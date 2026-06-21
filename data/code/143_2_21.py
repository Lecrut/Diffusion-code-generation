class ContradictionDetector:
    NEGATIVE_WORDS = {'not', 'cannot', 'no', 'never'}
    
    def __init__(self, statements):
        self.statements = statements
    
    def analyze_statements(self):
        positive_keywords = set()
        negative_keywords = set()
        
        for statement in self.statements:
            keywords = self.extract_keywords(statement)
            positive_keywords.update(keywords - self.NEGATIVE_WORDS)
            negative_keywords.update(self.NEGATIVE_WORDS.intersection(keywords))
        
        return positive_keywords, negative_keywords
    
    def extract_keywords(self, statement):
        words = set(statement.lower().split())
        return {word for word in words if word.isalpha() and len(word) > 3}
    
if __name__ == '__main__':
    detector = ContradictionDetector([
        "I can fly",
        "She cannot swim"
    ])
    positive, negative = detector.analyze_statements()
    print("Positive keywords:", positive)
    print("Negative keywords:", negative)