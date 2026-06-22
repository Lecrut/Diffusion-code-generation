class PrefixValidator:
    def __init__(self, targets):
        self.targets = tuple(targets)

    def contains_target_prefix(self, sequence):
        for item in sequence:
            if item and (item[0] == self.targets[0] or item[0] == self.targets[1]):
                return True
        return False

if __name__ == '__main__':
    validator = PrefixValidator(['A', 'B'])
    list_one = ['Apple', 'Dog', 'Cat']
    print(validator.contains_target_prefix(list_one))
    list_two = ['Dog', 'Elephant', 'Cat']
    print(validator.contains_target_prefix(list_two))