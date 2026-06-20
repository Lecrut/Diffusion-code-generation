class MutuallyExclusiveChecker:

    def __init__(self, states):
        self.states = states

    def is_mutually_exclusive(self):
        return sum(self.states) == 1
if __name__ == '__main__':
    checker1 = MutuallyExclusiveChecker({True, False})
    print(checker1.is_mutually_exclusive())
    checker2 = MutuallyExclusiveChecker({False, False})
    print(checker2.is_mutually_exclusive())
    checker3 = MutuallyExclusiveChecker({True, True})
    print(checker3.is_mutually_exclusive())
    checker4 = MutuallyExclusiveChecker({})
    print(checker4.is_mutually_exclusive())