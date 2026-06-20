class MutuallyExclusiveChecker:

    @staticmethod
    def check_single_activation(a: bool, b: bool) -> bool:
        return a != b
if __name__ == '__main__':
    print(MutuallyExclusiveChecker.check_single_activation(True, False))
    print(MutuallyExclusiveChecker.check_single_activation(False, True))
    print(MutuallyExclusiveChecker.check_single_activation(True, True))
    print(MutuallyExclusiveChecker.check_single_activation(False, False))