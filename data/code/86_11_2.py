class BooleanComparator:
    comparisons = {
        (True, True): 'Equal',
        (False, False): 'Equal',
        (True, False): 'Not Equal',
        (False, True): 'Not Equal'
    }

    def check_equality(self, a: bool, b: bool) -> str:
        return self.comparisons[(a, b)]

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))