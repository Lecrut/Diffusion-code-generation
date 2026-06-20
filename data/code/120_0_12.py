class EqualityChecker:
    def check_equality(self, a: any, b: any) -> bool:
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.check_equality(5, 5))
    print(checker.check_equality(10, 5))
    print(checker.check_equality("hello", "hello"))