class AttributeChecker:
    def __init__(self, values):
        self.values = values

    def check_attributes(self):
        attributes = {
            'a': {'check': lambda x: x > 0},
            'b': {'check': lambda x: x % 2 == 0},
            'c': {'check': lambda x: self.values['a'] != 0 and x % self.values['a'] == 0}
        }
        for attr, params in attributes.items():
            if not params['check'](self.values.get(attr, 0)):
                return False
        return True

if __name__ == '__main__':
    checker = AttributeChecker({'a': 5, 'b': 4, 'c': 10})
    print(checker.check_attributes())