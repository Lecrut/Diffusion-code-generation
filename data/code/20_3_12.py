class DivisibilityChecker:
    def __init__(self, value):
        self.value = value

    def is_divisible_by_two(self):
        if self.value == 0:
            return True
        if self.value < 0:
            self.value = -self.value
        return bool(self.value & 1) is False

if __name__ == '__main__':
    checker = DivisibilityChecker(42)
    print(checker.is_divisible_by_two())
    
    checker2 = DivisibilityChecker(21)
    print(checker2.is_divisible_by_two())
    
    checker3 = DivisibilityChecker(-8)
    print(checker3.is_divisible_by_two())
    
    checker4 = DivisibilityChecker(-7)
    print(checker4.is_divisible_by_two())
    
    checker5 = DivisibilityChecker(0)
    print(checker5.is_divisible_by_two())