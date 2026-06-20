class AttributeChecker:
    def __init__(self, values):
        self.values = values
    
    def check_attributes(self):
        a, b, c = self.values.get('a', 0), self.values.get('b', 0), self.values.get('c', 0)
        return a > 0 and b % 2 == 0 and c % a == 0

if __name__ == '__main__':
    checker = AttributeChecker({'a': 5, 'b': 4, 'c': 10})
    print(checker.check_attributes())