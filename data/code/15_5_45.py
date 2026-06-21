class KeyChecker:

    def __init__(self, data):
        self.data = data

    def check_identical_values(self, key1, key2):
        if key1 not in self.data or key2 not in self.data:
            raise KeyError(f'One or both keys ({key1}, {key2}) are missing from the dictionary.')
        return {key1: self.data[key1] == self.data[key2]}
if __name__ == '__main__':
    sample_data = {'alpha': 3, 'beta': 6, 'gamma': 3}
    checker = KeyChecker(sample_data)
    result1 = checker.check_identical_values('alpha', 'gamma')
    print(result1)
    result2 = checker.check_identical_values('beta', 'gamma')
    print(result2)