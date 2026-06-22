class PrefixValidator:
    def __init__(self, targets):
        self.targets = tuple(targets)

    def contains(self, source):
        for item in source:
            for char in self.targets:
                if item.startswith(char):
                    return True
        return False

if __name__ == '__main__':
    validator = PrefixValidator(['A', 'B'])
    test_set_one = ['Ant', 'Bear', 'Cat']
    test_set_two = ['Dog', 'Elephant', 'Fish']
    
    print(validator.contains(test_set_one))
    print(validator.contains(test_set_two))