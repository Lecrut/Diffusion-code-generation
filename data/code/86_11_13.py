class BooleanComparator:
    EQUALITY_MAP = {
        (True, True): 'Equal',
        (False, False): 'Equal',
        (True, False): 'Not Equal',
        (False, True): 'Not Equal'
    }
    
    @staticmethod
    def check_equality(a: bool, b: bool) -> str:
        return BooleanComparator.EQUALITY_MAP.get((a, b), 'Invalid Input')

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))