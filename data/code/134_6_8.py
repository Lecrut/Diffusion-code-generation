class MutuallyExclusiveChecker:
    @staticmethod
    def is_mutually_exclusive_set(s):
        return sum(s) == 1

if __name__ == '__main__':
    print(MutuallyExclusiveChecker.is_mutually_exclusive_set({True, False}))
    print(MutuallyExclusiveChecker.is_mutually_exclusive_set({False, False}))
    print(MutuallyExclusiveChecker.is_mutually_exclusive_set({True, True}))
    print(MutuallyExclusiveChecker.is_mutually_exclusive_set({}))