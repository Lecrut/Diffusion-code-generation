class ContradictionDetector:
    def __init__(self, statements):
        self.statements = statements

    def detect_contradictions(self):
        keywords = set()
        for statement in self.statements:
            words = statement.split()
            for word in words:
                if word.isalpha():
                    keywords.add(word.lower())
        
        contradictions = []
        for keyword in keywords:
            positive_statements = [s for s in self.statements if f"{keyword} " in s]
            negative_statements = [s for s in self.statements if f"not {keyword} " in s]
            if positive_statements and negative_statements:
                contradictions.append((keyword, positive_statements, negative_statements))
        
        return contradictions

if __name__ == '__main__':
    detector = ContradictionDetector([
        "The sky is blue",
        "Water is wet",
        "Birds can fly",
        "Fish can swim",
        "not Sky is not blue"
    ])
    
    print(detector.detect_contradictions())