class BooleanPresenceChecker:
    def __init__(self, source):
        self.source = source

    def verify_presence(self):
        return any(self.source)

if __name__ == '__main__':
    checker_a = BooleanPresenceChecker([0, 0, 0])
    print(checker_a.verify_presence())
    checker_b = BooleanPresenceChecker([0, 1, 0])
    print(checker_b.verify_presence())
    checker_c = BooleanPresenceChecker([])
    print(checker_c.verify_presence())
    checker_d = BooleanPresenceChecker([None, False, 0])
    print(checker_d.verify_presence())
    checker_e = BooleanPresenceChecker([None, False, 1])
    print(checker_e.verify_presence())