class SequenceEndChecker:
    def __init__(self, sequence):
        if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
            raise ValueError("Input must be a sequence type")
        self._sequence = sequence

    def get_endpoints(self):
        length = len(self._sequence)
        if length == 0:
            return None
        if length == 1:
            return (self._sequence[0], self._sequence[0])
        return (self._sequence[0], self._sequence[-1])

    def is_palindromic_end(self):
        endpoints = self.get_endpoints()
        if endpoints is None:
            return False
        return endpoints[0] == endpoints[1]

if __name__ == '__main__':
    checker = SequenceEndChecker([1, 2, 3, 4, 5])
    print(checker.get_endpoints())
    print(checker.is_palindromic_end())
    checker2 = SequenceEndChecker([1, 2, 3, 4, 1])
    print(checker2.get_endpoints())
    print(checker2.is_palindromic_end())
    checker3 = SequenceEndChecker("racecar")
    print(checker3.get_endpoints())
    print(checker3.is_palindromic_end())