class BooleanAnalyzer:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        return any(self.values)

    def count_true(self):
        return sum(self.values)

    def count_false(self):
        return len(self.values) - sum(self.values)

if __name__ == '__main__':
    analyzer = BooleanAnalyzer([False, False, False])
    print(analyzer.has_true())
    print(analyzer.count_true())
    print(analyzer.count_false())
    
    analyzer2 = BooleanAnalyzer([True, False, True])
    print(analyzer2.has_true())
    print(analyzer2.count_true())
    print(analyzer2.count_false())